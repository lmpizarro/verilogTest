import numpy as np
import twoCompl as twc

import matplotlib.pyplot as plt

class Pulse:
    IMAX = 0.005
    LAMBDA = 0.01

    FS = 100E6 
    VADC = 5.0
    NBITS = 14

    def setPmtComps(self, RES=1000, CAP=1E-9):
        self.RES = RES
        self.CAP = CAP 

    def calcConstants(self):
        self.TAO = self.CAP * self.RES
        self.TS = 1.0 / self.FS
        self.NOiSE = self.LAMBDA / 100.0
        self.RADC = np.power(2, self.NBITS)
        self.K2 = self.CAP / self.TS
        self.K1 = self.TS * self.RES /(self.TAO  + self.TS)

    def initLists(self, RINIT=1028):
        self.RINIT = RINIT
        self.RPULSE = 4096 * 2 - self.RINIT
        self.expPulse = []
        self.gaussianPulse = []
        self.pulseOut = []
        self.pulseOut.append(0)
        for i in range(self.RINIT):
            self.expPulse.append((.5 - np.random.random())*self.NOiSE)
            self.gaussianPulse.append(0)

    def calcPulseExp(self):
        for i in range(self.RPULSE):
            self.expPulse.append(self.IMAX*np.exp(-i*self.LAMBDA) + (.5-
                np.random.random())*self.NOiSE)

        self.expPulse.append(0)

    def calcPulseTri(self, WIDE = 500):
        N1=int(.2*WIDE)
        N2=WIDE-N1

        for i in range(N1):
            noise = (.5 - np.random.random())*self.NOiSE
            self.expPulse.append(self.IMAX * i / N1 + noise)
        for i in range(N2):
            noise = (.5 - np.random.random())*self.NOiSE
            self.expPulse.append(noise + self.IMAX - i * self.IMAX / N2)
        for i in range(self.RPULSE - N1 - N2):
            noise = (.5 - np.random.random())*self.NOiSE
            self.expPulse.append(noise)

    def calcPmtOut(self):
        for i in range(self.RINIT + self.RPULSE - 1):
            self.pulseOut.append((self.expPulse[i+1] + self.K2 * self.pulseOut[i])*self.K1)

    def calcADCOut(self, noise):
        for i,e in enumerate(self.pulseOut):
            self.pulseOut[i] = int(self.pulseOut[i] * self.RADC / self.VADC +
                    np.random.randint(-noise,noise))

    def calcPulse(self):
        for i in range(self.RPULSE):
            self.expPulse.append(self.IMAX*np.exp(-i*self.LAMBDA) + (.5-
                np.random.random())*self.NOiSE)
            T = (i-2000)
            if ( T < 0):
                self.gaussianPulse.append(self.IMAX*np.exp(-T**2/200000))
            else:
                self.gaussianPulse.append(0)

        self.expPulse.append(0)

        for i in range(self.RINIT + self.RPULSE - 1):
            self.pulseOut.append((self.expPulse[i+1] + self.K2 * self.pulseOut[i])*self.K1)


        for i,e in enumerate(self.pulseOut):
            self.pulseOut[i] = int(self.pulseOut[i] * self.RADC / self.VADC +
                    np.random.randint(-30,30))

def main():
    pulse = Pulse()
    pulse.setPmtComps()
    pulse.calcConstants()
    pulse.initLists()
    #pulse.calcPulseExp()
    pulse.calcPulseTri()
    pulse.calcPmtOut()
    pulse.calcADCOut(30)
    tw = twc.TwoCompl(16)
    twl = tw.toFile(pulse.pulseOut, "vector.tv")
    print twl
    plt.plot (pulse.pulseOut)
    plt.show()

if __name__ == "__main__":
        main()
