# Atividade ponderada m6.4

## arquivos

computer_vision.py: define uma função chamada `get_frame()` que captura quadros de uma câmera em tempo real usando a biblioteca OpenCV. Ele cria uma instância de `VideoCapture` para acessar a câmera e inicia um loop infinito para capturar continuamente os quadros. Cada quadro capturado é exibido em uma janela chamada 'frame' usando `cv2.imshow()` e é adicionado a uma lista chamada `frames`. O loop é interrompido quando a tecla 'q' é pressionada. Em seguida, a câmera é liberada e todas as janelas abertas são fechadas. Por fim, a função retorna a lista de quadros capturados. Em resumo, esse código permite obter uma lista de quadros capturados em tempo real a partir da câmera.


