import os, sys, platform
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")

print("python  :", sys.version.split()[0])
print("platform:", platform.platform(), platform.machine())
print("cpus    :", os.cpu_count())

import viennaps as vps
print("viennaps:", vps.version, "-- import OK")

vps.setDimension(2)
vps.Logger.setLogLevel(vps.LogLevel.ERROR)
vps.Length.setUnit("um"); vps.Time.setUnit("min")

for n in (1, 2, 4, os.cpu_count()):
    vps.setNumThreads(n)
    d = vps.Domain(gridDelta=0.06, xExtent=1.0,
                   boundary=vps.BoundaryType.REFLECTIVE_BOUNDARY)
    vps.MakeTrench(d, trenchWidth=0.4, trenchDepth=0.0, maskHeight=0.4).apply()
    m = vps.SF6O2Etching(ionFlux=12., etchantFlux=1.8e3, oxygenFlux=10.,
                         meanIonEnergy=100., sigmaIonEnergy=10., ionExponent=200.)
    p = vps.Process(d, m, 0.6)
    rp = vps.RayTracingParameters(); rp.raysPerPoint = 250
    p.setParameters(rp)
    p.apply()
    print(f"threads={n}: OK", flush=True)