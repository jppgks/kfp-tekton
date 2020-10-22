Patch pipeline-runner service account to be able to pull from ICR.
```shell script
oc get secret all-icr-io -n default -o yaml | sed 's/namespace: default/namespace: kubeflow/g' | oc -n kubeflow create -f -
oc patch serviceaccount pipeline-runner -p '{"imagePullSecrets": [{"name": "all-icr-io"}]}' -n kubeflow
```
