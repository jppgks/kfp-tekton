from kfp import dsl
from kubernetes import client as k8s_client


def echo_op(to_echo: str):
  return dsl.ContainerOp(
      name='icr-python-click-test',
      image='uk.icr.io/rxn-test/python-click-test:latest',
      command=['/bin/sh', '-c'],
      arguments=[f'/opt/conda/bin/python print_arg.py --demo-arg "{to_echo}"']
  )


@dsl.pipeline(name='echo', description='echo pipeline')
def echo_pipeline(to_echo: str = 'Got scheduled'):
  echo = echo_op(to_echo)

  dsl.get_pipeline_conf() \
      .set_image_pull_secrets([k8s_client.V1ObjectReference(name="all-icr-io")])


if __name__ == '__main__':
  from kfp_tekton.compiler import TektonCompiler

  TektonCompiler().compile(echo_pipeline, 'echo_pipeline.yaml')
