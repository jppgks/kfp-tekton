import click


@click.command()
@click.option('--demo-arg', default='Hello', help='Value to be printed')
def main(demo_arg):
  print(demo_arg)


if __name__ == '__main__':
  main()
