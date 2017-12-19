__author__ = 'robbielynch'

# from IPython.kernel.zmq.kernelbase import Kernel
# from ipykernel.zmq.kernelbase import Kernel
from ipykernel.kernelbase import Kernel
from bfinterpreter.brainfuck import Brainy

# StdIO 都被劫走了,只好用 beep 來 debug 看 有來/沒來 也好
# https://stackoverflow.com/questions/4467240/play-simple-beep-with-python-without-external-library
# import winsound         # for sound  
# import time             # for sleep
# winsound.Beep(440, 250) # frequency, duration
# time.sleep(0.25)        # in seconds (0.25 is 250ms)
# winsound.Beep(600, 250)
# time.sleep(0.25)
import peforth
peforth.vm.dictate('''
    import winsound constant winsound // ( -- module ) 
    : beep winsound :: Beep(pop(),50) ;
    1000 beep 800 beep 500 beep
    ''')
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class BrainfuckKernel(Kernel):
    peforth.vm.dictate('500 beep 500 beep 500 beep')
    logger.info("BrainfuckKernel-11") # debug
    implementation = 'brainfuck'
    implementation_version = '1.0'
    language = 'brainfuck'
    language_version = '0.1'
    language_info = {'mimetype': 'text/plain', 'name': 'brainfuck'}
    banner = "Brainfuck Kernel - it fucks with your brain"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        peforth.vm.dictate('800 beep 800 beep 800 beep')
        logger.info("do_execute-22") # debug
        if not silent:
            peforth.vm.dictate('1800 beep 1800 beep 1800 beep')
            brainy = Brainy()
            brainy.eval(code)
            code_result = brainy.get_output()
            logger.info("do_execute-33" + code_result) # debug
            stream_content = {'name': 'stdout', 'text': code_result}
            self.send_response(self.iopub_socket, 'stream', stream_content)
        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

if __name__ == '__main__':
    # from IPython.kernel.zmq.kernelapp import IPKernelApp
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=BrainfuckKernel)
else:
    # from IPython.kernel.zmq.kernelapp import IPKernelApp
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=BrainfuckKernel)