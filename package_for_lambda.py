import os
import tempfile
import shutil


def main():
    # make temp dir
    cwd = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=cwd)

    # find files
    ask_alexa_pykit_src = os.path.join(cwd, 'ask-alexa-pykit/ask')
    ask_alexa_pykit_dest = os.path.join(temp_dir, 'ask')
    lambda_handler = os.path.join(cwd, 'lambda_function.py')

    # copy em
    shutil.copy(lambda_handler, temp_dir)
    shutil.copytree(ask_alexa_pykit_src, ask_alexa_pykit_dest,
                    ignore=shutil.ignore_patterns('*.pyc', '*.git*', 'config', 'data'))

    # zip it
    shutil.make_archive('lambda', 'zip', root_dir=temp_dir)

    # cleanup
    shutil.rmtree(temp_dir)  # cleanup


if __name__ == '__main__':
    main()
