"""Check resource paths, declared sizes, SHA-256 hashes and chunked model manifests."""
from pathlib import Path
import hashlib,json,struct
ROOT=Path(__file__).resolve().parents[1]

def main():
    catalog=json.loads((ROOT/'resources.json').read_text());seen=set();checked={}
    def path(name):
        p=(ROOT/name).resolve()
        if not p.is_relative_to(ROOT) or not p.is_file():raise ValueError('Missing or escaping resource: '+name)
        return p
    def check(p,size,sha):
        if p not in checked:
            with p.open('rb') as f:checked[p]=(p.stat().st_size,hashlib.file_digest(f,'sha256').hexdigest())
        if checked[p]!=(size,sha):raise ValueError('Resource differs from checksum: '+str(p))
    for resource in catalog['resources']:
        if resource['id'] in seen:raise ValueError('Duplicate resource ID')
        seen.add(resource['id'])
        prefix='project/'+resource['scene_id']+'/'+resource['category']+'/'+resource['version']+'/'
        for asset in resource['assets']:
            if not asset['path'].startswith(prefix):raise ValueError('Resource path differs from ownership/version')
            check(path(asset['path']),asset['bytes'],asset['sha256'])
        if resource['format']=='glb_parts':
            for key in ('manifest','compatibility_manifest'):
                file=path(resource[key]);manifest=json.loads(file.read_text());total=0
                for part in manifest['parts']:
                    p=path(str((file.parent/part['file']).relative_to(ROOT)));check(p,part['bytes'],part['sha256']);total+=part['bytes']
                if total!=manifest['total_bytes'] or total!=resource['total_bytes']:raise ValueError('Incorrect assembled model size')
                with (file.parent/manifest['parts'][0]['file']).open('rb') as f:magic,version,length=struct.unpack('<4sII',f.read(12))
                if (magic,version,length)!=(b'glTF',2,total):raise ValueError('Invalid GLB header or assembled length')
        elif resource['format']=='glb':
            with path(resource['entry']).open('rb') as f:magic,version,length=struct.unpack('<4sII',f.read(12))
            if (magic,version,length)!=(b'glTF',2,path(resource['entry']).stat().st_size):raise ValueError('Invalid GLB')
    for file in (ROOT/'project').glob('*/resources.json'):
        scene=json.loads(file.read_text())
        if set(scene['resource_ids'])!={r['id'] for r in catalog['resources'] if r['scene_id']==scene['scene_id']}:raise ValueError('Scene index differs from catalogue')
    print(f'VALID: {len(seen)} resource versions; {len(checked)} files; sizes, SHA-256 and GLB containers checked.')

if __name__=='__main__':main()
