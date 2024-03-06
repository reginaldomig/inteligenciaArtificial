
import colorsys as cl
import turtle as tt

tt.Screen()
tt.shape('classic')
tt.speed(30)
tt.tracer(2)
tt.pensize(1)
passo = 0

cor_muda = 0.0



while True:
    
    tt.pencolor(cl.hls_to_rgb(cor_muda,cor_muda,cor_muda))
    tt.fd(passo)
    tt.left(120)
    passo += 1
    cor_muda += 0.01
    if(cor_muda >= 0.999):
        cor_muda = 0.0



tt.done()