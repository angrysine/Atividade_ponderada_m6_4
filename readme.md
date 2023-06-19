# Atividade ponderada m6.4

## arquivos

computer_vision.py: define uma função chamada `get_frame()` que captura quadros de uma câmera em tempo real usando a biblioteca OpenCV. Ele cria uma instância de `VideoCapture` para acessar a câmera e inicia um loop infinito para capturar continuamente os quadros. Cada quadro capturado é exibido em uma janela chamada 'frame' usando `cv2.imshow()` e é adicionado a uma lista chamada `frames`. O loop é interrompido quando a tecla 'q' é pressionada. Em seguida, a câmera é liberada e todas as janelas abertas são fechadas. Por fim, a função retorna a lista de quadros capturados. Em resumo, esse código permite obter uma lista de quadros capturados em tempo real a partir da câmera.

send_images.py :Este código utiliza a biblioteca Ultralytics e OpenCV para processar quadros capturados de uma câmera. Primeiro, ele chama a função get_frame() para obter uma lista de quadros da câmera. Em seguida, um modelo YOLO é carregado utilizando o arquivo yolov8n-face.pt. Em um loop, cada quadro da lista é passado para o modelo YOLO, gerando previsões. A imagem resultante com as previsões é salva em um arquivo PNG. O quadro também é lido novamente, convertido para base64 e enviado para um servidor através de uma requisição POST para o endereço "<http://127.0.0.1:5000/>". A resposta JSON do servidor é impressa. O loop continua até que todos os quadros da lista tenham sido processados. Em resumo, o código processa os quadros da câmera utilizando o modelo YOLO e envia as imagens com previsões para um servidor.

main.py:Este código cria uma aplicação Flask que recebe requisições HTTP. Ele utiliza a biblioteca supabase para criar um cliente que se conecta a uma instância do Supabase, um serviço de banco de dados. A aplicação possui duas rotas:

Rota POST ("/"): Quando um cliente faz uma requisição POST para essa rota, o código lê os dados enviados na requisição. Ele extrai uma imagem codificada em base64 e o nome da imagem do corpo da requisição JSON. Em seguida, ele decodifica a imagem base64 e a salva como um arquivo PNG chamado "image.png". O arquivo de imagem é então enviado para o Supabase Storage, utilizando o caminho "/autoestudo/images" e o nome fornecido na requisição. A resposta da operação de upload é retornada como uma mensagem JSON.

A aplicação Flask é executada quando o código é executado diretamente, e fica em execução no modo de depuração.

## como executar

entre na pasta do projeto e execute o comando:

```bash
python main.py
```

depois execute:

```bash
python send_images.py
```

## video

link do drive: <https://drive.google.com/file/d/14FbjKUUmAkM9QadpEwVedHRDs17peYXu/view?usp=sharing>
