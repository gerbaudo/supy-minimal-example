import calculable_example
import supy
import ROOT as r


class example_analysis(supy.analysis):
    def listOfSteps(self, config):
        sshv = supy.steps.histos.value
        return [supy.steps.printer.progressPrinter(),
                sshv('run', 20, 0, 1e4),
                sshv('bx', 3564, 0., 3564.),
                sshv('Two', 10, 0, 10),
                sshv('nTracksV0',50+1, -0.5, +50.5),
                supy.calculables.other.Ratio("nTracksV0", binning = (50+1,-0.5,50.5),
                                             thisSample = 'MC', target = ('Data',[])),
                #supy.steps.printer.printstuff(['threeWeights']),
                supy.steps.other.reweights(sshv('nTracksV0',50+1, -0.5, +50.5), 'threeWeights', 3),
                ]

    def listOfCalculables(self, config):
        return (supy.calculables.zeroArgs(supy.calculables) +
                [supy.calculables.other.fixedValue('Two', 2)] +
                [calculable_example.nTracksV0(),
                 calculable_example.threeWeights(),
                 ]
                )

    def listOfSampleDictionaries(self):
        dir = "data"
        holder = supy.samples.SampleHolder()

        holder.add("Data",
                   '["%s/skimmed_900_GeV_Data.root"]' % dir,
                   lumi=1.0e-5,  # /pb
                   )
        holder.add("MC",
                   '["%s/skimmed_900_GeV_MC.root"]' % dir,
                   xs=1.0e8,  # pb
                   )
        return [holder]

    def listOfSamples(self, config):
        return (supy.samples.specify(names="Data",
                                     color=r.kBlack,
                                     markerStyle=20) +
                supy.samples.specify(names="MC",
                                     color=r.kRed,
                                     effectiveLumi=0.5,
                                     weights='nTracksV0Ratio')
                )

    def conclude(self, pars):
        #make a pdf file with plots from the histograms created above
        org = self.organizer(pars)
        org.scale()
        supy.plotter(org,
                     pdfFileName=self.pdfFileName(org.tag),
                     samplesForRatios=("Data", "MC"),
                     sampleLabelsForRatios=("data", "sim"),
                     detailedCalculables=True,
                     ).plotAll()
