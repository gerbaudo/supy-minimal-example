git clone --recursive git://github.com/<user>/supy-minimal-example  # clone repo: <user> can be davidegerbaudo or a forking user
cd supy-minimal-example
# git submodule update                                  # checkout supy dependence (only needed if '--recursive' was not used)
export PYTHONPATH=$PYTHONPATH:`pwd`                     # add directory containing supy to your python path
export PATH=$PATH:`pwd`/supy/bin                        # optionally add to your path
supy example_analysis.py --loop 1                       # run the example (the example input files are located on AFS)
