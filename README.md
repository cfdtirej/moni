# moni

[nginx-prometheus-exporter](https://github.com/nginxinc/nginx-prometheus-exporter) と Prometheusを使ってNginxを監視

## 起動手順

> Clusterの作成
```shell
kind create cluster --config cluster.yaml
```

> Ingress-Controllerの作成

```shell
kubectl apply -f \
  https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

> 実行中のリクエストを処理する準備ができるまで待機

```shell
kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=90s
```

> metrics-serverの導入

```shell
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

> Kubernetes起動

```shell
# 純粋なマニフェストを使う場合
kubectl apply -f .k8s

# kustomizeを使う場合
kustomize build .kustomize/overlays/prod | kubectl apply -f -
```

> metrics-server起動
- HPAでメトリクスを収集するためにはmetrics-serverを起動する必要がある
- kindで構築すると[ドキュメント通りに実行](https://github.com/kubernetes-sigs/metrics-server#installation)しても動かない
- `args`に`- --kubelet-insecure-tls`を追加すると動くようなので、[metrics-serverのマニフェスト](https://github.com/kubernetes-sigs/metrics-server/tree/master/manifests/base)を編集した`metrics-server.yaml`を作成

```shell
kubectl apply -f .kustomize/other/metrics-server.yaml
```

> 参考
- Clusterの作成
  - https://kind.sigs.k8s.io/docs/user/ingress/#contour
- NginxIngressController
  - https://kind.sigs.k8s.io/docs/user/ingress/#ingress-nginx
  - https://kubernetes.github.io/ingress-nginx/deploy/#docker-desktop
- metrics-server
  - https://github.com/kubernetes-sigs/metrics-server/blob/master/README.md
