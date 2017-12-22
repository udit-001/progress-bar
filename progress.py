import time
import sys
import winsound


##for i in range(11):
##    time.sleep(2)
##    if i == 10:
##        sys.stdout.write('Loading Completed!')
##    else:
##        sys.stdout.write('Loading {}%...\r'.format(i*10))
##    sys.stdout.flush()


##print('\n')
##for i in range(11):
##    time.sleep(1)
##    if i == 10:
##        sys.stdout.write(' '+'#'*i+'Completed!')
##    else:
##        sys.stdout.write(' '+'#'*i+'{}%...\r'.format(i*10))
##    sys.stdout.flush()

delay = 0.2
string = ' Progress : ['
progress = 0
style = '#'
for i in range(1,11):
    result = 10 - i
    sys.stdout.write(string+'|'+'-'*result+']{}%\r\r'.format(progress+int(10/6*1)))
    sys.stdout.flush()
    time.sleep(delay)
    sys.stdout.write(string+'/'+'-'*result+']{}%\r\r'.format(progress+int(10.0/6*2)))
    sys.stdout.flush()
    time.sleep(delay)
    sys.stdout.write(string+'-'+'-'*result+']{}%\r\r'.format(progress+int(10.0/6*3)))
    sys.stdout.flush()
    time.sleep(delay)
    sys.stdout.write(string+'\\'+'-'*result+']{}%\r\r'.format(progress+int(10.0/6*4)))
    sys.stdout.flush()
    time.sleep(delay)
    sys.stdout.write(string+'-'+'-'*result+']{}%\r\r'.format(progress+int(10.0/6*5)))
    sys.stdout.flush()
    time.sleep(delay)
    sys.stdout.write(string+style+'-'*result+']{}%\r\r'.format(progress+int(10.0/6*6)))
    string += style
    sys.stdout.flush()
    progress = i*10

print('\n\a\a Download Completed!')

