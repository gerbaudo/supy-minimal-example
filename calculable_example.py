import supy

class nTracksV0(supy.wrappedChain.calculable) :
    def update(self,_) :
        ntrk = self.source["vertexNtrks"]
        self.value = ntrk[0] if len(ntrk) else 0

class threeWeights(supy.wrappedChain.calculable) :
    def update(self,_) :
        ntkR = self.source['nTracksV0Ratio']
        self.value = [ntkR, 1./ntkR if ntkR else 1.0, 2.0]
