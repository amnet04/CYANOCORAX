import wavio
from scipy.signal import decimate

rate, sampwidth,  data=wavio.readwav('/home/eudocio/Escritorio/borrar/EHB/Cuestionarios/121 (AUDIO A).wav')
decimationFactor=2
nframes=len(data)
subSamplingData=decimate(data, decimationFactor, 1,'fir', axis=0)
monoAverage=data.mean(axis=1)
monoLeft=data[:, 0]
monoRight=data[:, 1]
wavio.writewav24('/home/eudocio/Escritorio/borrar/EHB/Cuestionarios/121_AUDIO_A_decimado.wav', 24000, subSamplingData)
wavio.writewav24('/home/eudocio/Escritorio/borrar/EHB/Cuestionarios/121_AUDIO_A_nuevo.wav', 48000, monoAverage)
wavio.writewav24('/home/eudocio/Escritorio/borrar/EHB/Cuestionarios/121_AUDIO_A_izquierdo.wav', 48000, monoLeft)
wavio.writewav24('/home/eudocio/Escritorio/borrar/EHB/Cuestionarios/121_AUDIO_A_derecho.wav', 48000, monoRight)
print(subSamplingData)
