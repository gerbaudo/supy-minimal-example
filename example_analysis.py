import supy
import ROOT as r


class example_analysis(supy.analysis):
    def listOfSteps(self, config):
        return [supy.steps.printer.progressPrinter(),
                supy.steps.histos.value('run', 20, 0, 1e4),
                supy.steps.histos.value('bx', 3564, 0., 3564.),
                supy.steps.histos.value('Two', 10, 0, 10),
                ]

    def listOfCalculables(self, config):
        return (supy.calculables.zeroArgs(supy.calculables) +
                [supy.calculables.other.fixedValue('Two', 2)]
                )

    def listOfSampleDictionaries(self):
        dir = "/afs/cern.ch/user/e/elaird/public/susypvt/framework_take3/"
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
                                     effectiveLumi=0.5)
                )

    def conclude(self, pars):
        #make a pdf file with plots from the histograms created above
        org = self.organizer(pars)
        org.scale()
        supy.plotter(org,
                     pdfFileName=self.pdfFileName(org.tag),
                     samplesForRatios=("Data", "MC"),
                     sampleLabelsForRatios=("data", "sim"),
                     ).plotAll()
