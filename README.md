# CartoonizedGanAPI
`CartoonizedGan` 을 대상으로 `Flask` 를 활용하여, model 을 API 화 합니다.



#### Dev

- `python app.py` 
- `Swagger`-> http://localhost:8080/swagger/

<img src="./sample/swagger_example.gif" alt="swagger_example" style="zoom:50%;" />

- 개발용 시뮬레이션 Docker

```shell

# docker build
docker build -f DevDockerfile --tag dev_cartoonize_api:1.0 .

# docker run 
docker run -p 8080:8080 dev_cartoonize_api:1.0

```









### Prod

- `Gunicorn - Gthread` 를 활용하여 진행합니다. 

- Prod 용 Docker

  ```shell
  
  # docker build
  docker build -f Dockerfile --tag cartoonize_api:1.0 .
  
  # docker run 
  docker run -p 8080:8080 cartoonize_api:1.0
  
  ```

- Docker 로 실행하고, client.py 를 실행시켜서, 제대로 동작하는 지 확인가능. 

- Elastic Beanstalk 를 활용하여, 배포하기 위해서 필요한 부분 구현완료. 



