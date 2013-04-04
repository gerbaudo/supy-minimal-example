Follow these commands to set up and test supy locally.

```bash
git clone --recursive git://github.com/<user>/supy-minimal-example  # clone repo: <user> can be davidegerbaudo or a forking user
cd supy-minimal-example
git submodule update --init           # checkout supy dependence (only needed if '--recursive' was not used)
source env.sh                         # add directory containing supy to your python path; optionally add supy/bin to your path

supy-test                             # run supy test suite (optional)
supy example_analysis.py --loop 1     # run the example
```