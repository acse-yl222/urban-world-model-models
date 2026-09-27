# Resource repository instructions

Keep computation and viewer implementations in the framework repository. Group assets
under project/<scene>/<category>/<version>, using canonical scene IDs. Register every
file in resources.json with byte size and SHA-256, plus source repository/revision/path.
Keep versions immutable and preserve manifest compatibility when relocating files.
Do not replace missing scientific provenance or licensing information with assumptions.
Never publish private local data by inference. Run python3 tools/check_resources.py
before publishing. Update the scene index and browser catalogue together.
