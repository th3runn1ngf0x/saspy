#
# Copyright SAS Institute
#
#  Licensed under the Apache License, Version 2.0 (the License);
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

# THIS IS AN EXAMPLE CONFIG FILE. PLEASE CREATE YOUR OWN sascfg_personal.py FILE USING THE APPROPRIATE TEMPLATES FROM BELOW
# SEE THE CONFIGURATION DOC AT https://sassoftware.github.io/saspy/install.html#configuration


# Configuration Names for SAS - python List
# This is the list of allowed configuration definitions that can be used. The definition are defined below.
# if there is more than one name in the list, and cfgname= is not specified in SASsession(), then the user
# will be prompted to choose which configuration to use.
#
# The various options for the different access methods can be specified on the SASsession() i.e.:
# sas = SASsession(cfgname='default', options='-fullstimer', user='me')
#
# Based upon the lock_down configuration option below, you may or may not be able to override option
# that are defined already. Any necessary option (like user, pw for IOM or HTTP) that are not defined will be 
# prompted for at run time. To dissallow overrides of as OPTION, when you don't have a value, simply
# specify options=''. This way it's specified so it can't be overridden, even though you don't have any
# specific value you want applied.
# 
#SAS_config_names = ['default', 'ssh', 'iomlinux', 'iomwin', 'winlocal', 'winiomlinux', 'winiomwin', 'httpsviya', 'httpviya', 'iomcom']
#

SAS_config_names=['default']

# Configuration options for saspy - python Dict
# valid key are:
# 
# 'lock_down' - True | False. True = Prevent runtime overrides of SAS_Config values below
#
# 'verbose'   - True | False. True = Allow print statements for debug type messages
#
SAS_config_options = {'lock_down': False,
                      'verbose'  : True
                     }

# Configuration options for SAS output. By default output is HTML 5.0 (using "ods html5" statement) but certain templates might not work 
# properly with HTML 5.0 so it can also be set to HTML 4.0 instead (using "ods html" statement). This option will only work when using IOM
# in local mode. Note that HTML 4.0 will generate images separately which clutters the workspace and if you download the notebook as HTML, 
# the HTML file will need to be put in the same folder as the images for them to appear.
# valid key are:
# 
# 'output' = ['html5', 'html']
#
SAS_output_options = {'output' : 'html5'}


# Configuration Definitions
#
# For STDIO and STDIO over SSH access methods
# These need path to SASHome and optional startup options - python Dict
# The default path to the sas start up script is: /opt/sasinside/SASHome/SASFoundation/9.4/sas
# A usual install path is: /opt/sasinside/SASHome
#
# Since python uses utf-8, running SAS with encoding=utf-8 is the expected use case. By default Unix SAS runs in Latin1 (iso-8859-1),
# which does not work well as utf-8. So, transcoding has been implemented in the python layer. The 'encoding' option can be specified to match
# the SAS session encoding (see https://docs.python.org/3.5/library/codecs.html#standard-encodings for python encoding values). latin1 is appropriate
# for the default Unix SAS session encoding
#                                                                                                         
# valid keys are:
# 'saspath'  - [REQUIRED] path to SAS startup script i.e.: /opt/sasinside/SASHome/SASFoundation/9.4/sas
# 'options'  - SAS options to include in the start up command line - Python List
# 'encoding' - This is the python encoding value that matches the SAS session encoding your SAS session is using 
#
# For passwordless ssh connection, the following are also reuqired:
# 'ssh'     - [REQUIRED] the ssh command to run
# 'host'    - [REQUIRED] the host to connect to
#
# Additional valid keys for ssh:
# 'port'    - [integer] the remote ssh port
# 'tunnel'  - [integer] local port to open via reverse tunnel, if remote host cannot otherwise reach this client
#
default  = {'saspath'  : '/opt/sasinside/SASHome/SASFoundation/9.4/bin/sas_u8'
            }

ssh      = {'saspath' : '/opt/sasinside/SASHome/SASFoundation/9.4/bin/sas_en',
            'ssh'     : '/usr/bin/ssh',
            'host'    : 'remote.linux.host', 
            'encoding': 'latin1',
            'options' : ["-fullstimer"]
            }


# For IOM (Grid Manager or any IOM) and Local Windows via IOM access method
# These configuration definitions are for connecting over IOM. This is designed to be used to connect to any Workspace server, including SAS Grid, via Grid Manager
# and also to connect to a local Windows SAS session. The client side (python and java) for this access method can be either Linux or Windows.
# The STDIO access method above is only for Linux. PC SAS requires this IOM interface.
#
# The absence of the iomhost option triggers local Windows SAS mode. In this case none of 'iomhost', 'iomport', 'omruser', 'omrpw' are needed.
# a local SAS session is started up and connected to.
#
# Since python uses utf-8, running SAS with encoding=utf-8 is the expected use case. By default Windows SAS runs in WLatin1 (windows-1252),
# which does not work well as utf-8. So, transcoding has been implemented in the python layer. The 'encoding' option can be specified to match
# the SAS session encoding (see https://docs.python.org/3.5/library/codecs.html#standard-encodings for python encoding values). windows-1252 is appropriate
# for the default Windows SAS session encoding
#                                                                                                         

#
# NEW IN V3.3.3!!!  No longer need the classpath, as the 4 IOM client jars are now included in the saspy repo. saspy will generate the classpath itself.
# If your workspace server is configured to use Encryption then you still need to get those 3 jars from your SAS install and code the full classpath. 
# But most cases aren't set up encryption, so for most cases, you no loinger need to provice the classpath
#

###### Pre- V3.3.3:  Since this IOM access method uses the Java IOM client, a classpath is required for the java process to find the necessary jars. Use the template below
###### to build out a classpath variable and assign that to the 'classpath' option in the configuration definition. The IOM client jars are delivered as part
###### of a Base SAS install, so should be available in any SAS install. The saspyiom.jar is available in the saspy repo/install. 
#
# NONE OF THE PATHS IN THESE EAMPLES ARE RIGHT FOR YOUT INSTALL. YOU HAVE TO CHANGE THE PATHS TO BE CORRECT FOR YOUR INSTALLATION 
#
# valid keys are:
# 'java'      - [REQUIRED] the path to the java executable to use
# 'iomhost'   - [REQUIRED for remote IOM case, Don't specify to use a local Windows Session] the resolvable host name, or ip to the IOM server to connect to
# 'iomport'   - [REQUIRED for remote IOM case, Don't specify to use a local Windows Session] the port IOM is listening on
# 'authkey'   - identifier for user/password credentials to read from .authinfo file. Eliminates prompting for credentials.
# 'omruser'   - not suggested        [REQUIRED for remote IOM case but PROMPTED for at runtime] Don't specify to use a local Windows Session
# 'omrpw'     - really not suggested [REQUIRED for remote IOM case but PROMPTED for at runtime] Don't specify to use a local Windows Session
# 'encoding'  - This is the python encoding value that matches the SAS session encoding of the IOM server you are connecting to
# 'classpath' - [REQUIRED] classpath to IOM client jars and saspy client jar.
# 'appserver' - name of physical workspace server (when more than one app server defined in OMR) i.e.: 'SASApp - Workspace Server'
# 'sspi'      - boolean. use IWA instead of user/pw to connect to the IOM workspace server


# build out a local classpath variable to use below for Linux clients  CHANGE THE PATHS TO BE CORRECT FOR YOUR INSTALLATION 
cpL  =  "/opt/github/saspy/java/saspyiom.jar"
cpL += ":/opt/github/saspy/java/iomclient/sas.svc.connection.jar"
cpL += ":/opt/github/saspy/java/iomclient/log4j.jar"
cpL += ":/opt/github/saspy/java/iomclient/sas.security.sspi.jar"
cpL += ":/opt/github/saspy/java/iomclient/sas.core.jar"

iomlinux = {'java'      : '/usr/bin/java',
            'iomhost'   : 'linux.iom.host',
            'iomport'   : 8591,
            'encoding'  : 'latin1',
            #'classpath' : cpL
            }           

iomwin   = {'java'      : '/usr/bin/java',
            'iomhost'   : 'windows.iom.host',
            'iomport'   : 8591,
            'encoding'  : 'windows-1252',
            #'classpath' : cpL
            }

         
# build out a local classpath variable to use below for Windows clients   CHANGE THE PATHS TO BE CORRECT FOR YOUR INSTALLATION 
cpW  =  "C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\saspy\\java\\saspyiom.jar"
cpW += ";C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\saspy\\java\\iomclient\\sas.svc.connection.jar"
cpW += ";C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\saspy\\java\\iomclient\\log4j.jar"
cpW += ";C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\saspy\\java\\iomclient\\sas.security.sspi.jar"
cpW += ";C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\saspy\\java\\iomclient\\sas.core.jar"

# These jars provide CORBA support for Java 10+ which no longer provides CORBA itself.  CHANGE THE PATHS TO BE CORRECT FOR YOUR INSTALLATION 
cpW += ";C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\saspy\\java\\thirdparty\\glassfish-corba-internal-api.jar"
cpW += ";C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\saspy\\java\\thirdparty\\glassfish-corba-omgapi.jar"
cpW += ";C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\saspy\\java\\thirdparty\\glassfish-corba-orb.jar"
cpW += ";C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\saspy\\java\\thirdparty\\pfl-basic.jar"
cpW += ";C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\saspy\\java\\thirdparty\\pfl-tf.jar"

# And, if you've configured IOM to use Encryption, you need these client side jars.  CHANGE THE PATHS TO BE CORRECT FOR YOUR INSTALLATION 
#cpW += ";C:\\Program Files\\SASHome\\SASVersionedJarRepository\\eclipse\\plugins\\sas.rutil_904300.0.0.20150204190000_v940m3\\sas.rutil.jar"
#cpW += ";C:\\Program Files\\SASHome\\SASVersionedJarRepository\\eclipse\\plugins\\sas.rutil.nls_904300.0.0.20150204190000_v940m3\\sas.rutil.nls.jar"
#cpW += ";C:\\Program Files\\SASHome\\SASVersionedJarRepository\\eclipse\\plugins\\sastpj.rutil_6.1.0.0_SAS_20121211183517\\sastpj.rutil.jar"


winlocal = {'java'      : 'java',
            'encoding'  : 'windows-1252',
            #'classpath' : cpW
            }

winiomlinux = {'java'   : 'java',
            'iomhost'   : 'linux.iom.host',
            'iomport'   : 8591,
            'encoding'  : 'latin1',
            #'classpath' : cpW
            }

winiomwin  = {'java'    : 'java',
            'iomhost'   : 'windows.iom.host',
            'iomport'   : 8591,
            'encoding'  : 'windows-1252',
            #'classpath' : cpW
            }

winiomIWA  = {'java'    : 'java',
            'iomhost'   : 'windows.iom.host',
            'iomport'   : 8591,
            'encoding'  : 'windows-1252',
            #'classpath' : cpW,
            'sspi'      : True
            }


# For Remote and Local IOM access methods using COM interface
# These configuration definitions are for connecting over IOM using COM. This
# access method is for Windows clients connecting to remote hosts. Local
# SAS instances may also be supported.
#
# This access method does not require a Java dependency.
#
# Valid Keys:
#   iomhost     - Required for remote connections only. The Resolvable SAS
#                 server dns name.
#   iomport     - Required for remote connections only. The SAS workspace
#                 server port. Generally 8591 on standard remote
#                 installations. For local connections, 0 is the default.
#   class_id    - Required for remote connections only. The IOM workspace
#                 server class identifier. Use `PROC IOMOPERATE` to identify
#                 the correct value. This option is ignored on local connections.
#   provider    - [REQUIRED] IOM provider. "sas.iomprovider" is recommended.
#   encoding    - This is the python encoding value that matches the SAS
#                 session encoding of the IOM server.
#   omruser     - SAS user. This option is ignored on local connections.
#   omrpw       - SAS password. This option is ignored on local connections.
#   authkey     - Identifier for credentials to read from .authinfo file.

iomcom = {
    'iomhost' : 'mynode.mycompany.org',
    'iomport' : 8591,
    'class_id': '440196d4-90f0-11d0-9f41-00a024bb830c',
    'provider': 'sas.iomprovider',
    'encoding': 'windows-1252'}


# HTTP access method to connect to the Compute Service
# These need ip addr, other values will be prompted for - python Dict
# valid keys are:
# 'ip'      - [REQUIRED] host address 
# 'port'    - port; the code Defaults this to based upon the 'ssl' key; 443 default else 80
# 'ssl'     - whether to use HTTPS or just HTTP protocal. Default is True, using ssl and poort 443
# 'context' - context name defined on the compute service  [PROMTED for at runtime if more than one defined]
# 'authkey' - identifier for user/password credentials to read from .authinfo file. Eliminates prompting for credentials.
# 'options' - SAS options to include (no '-' (dashes), just option names and values)
# 'user'    - not suggested [REQUIRED but PROMTED for at runtime]
# 'pw'      - really not suggested [REQUIRED but PROMTED for at runtime]
# 
#
             
httpsviya = {'ip'      : 'sastpw.rndk8s.openstack.sas.com',
             'context' : 'Data Mining compute context',
             'authkey' : 'viya_user-pw',
             'options' : ["fullstimer", "memsize=1G"]
             }

httpviya = {'ip'      : 'sastpw.rndk8s.openstack.sas.com',
            'ssl'     : False,  # this will use port 80
            'context' : 'Data Mining compute context',
            'authkey' : 'viya_user-pw',
            'options' : ["fullstimer", "memsize=1G"]
            }
