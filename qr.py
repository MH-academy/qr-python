import qrcode

tecnologias = ['Python', 'Javascript', 'Java', 'Html']

print('QR Generator')
print('salvando códigos...')

for valores in tecnologias:

  print('.')

  img = qrcode.make(valores)
  type(img)
  path = valores + '.png'
  img.save('codes/'+ path)

print('salvo com sucesso')

