# moni

[nginx-prometheus-exporter](https://github.com/nginxinc/nginx-prometheus-exporter) と Prometheusを使ってNginxを監視


## 起動手順
```shell
# Clusterの作成
$ kind create cluster --config cluster.yaml

# Ingress-Controllerの作成
$ kubectl apply -f \
  https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml

# kind(k8s in docker)でIngressを使うときの設定
$ kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=90s

# Kubernetes起動
$ kubectl apply -f .k8s
```

> 参考
- Clusterの作成
  - https://kind.sigs.k8s.io/docs/user/ingress/#contour
- IngressControllerの作成
  - https://kind.sigs.k8s.io/docs/user/ingress/#ingress-nginx
  - https://kubernetes.github.io/ingress-nginx/deploy/#docker-desktop
- kind(k8s in docker)でIngressを使うときの設定
  - https://kind.sigs.k8s.io/docs/user/ingress/#ingress-nginx
