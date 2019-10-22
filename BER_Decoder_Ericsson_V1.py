__author__ = 'mraouf'

import time
import  asn1tools

start_time_total = time.time()
##### Output File Directory #######
output_Directory=open("E:\\3.Etisalat UAE\\13.Etisalat_GitHub_Scripts\\Decoded_configuration.txt","w")

######## Importing the Schema File needed for Decoding ############
foo = asn1tools.compile_files('E:\\3.Etisalat UAE\\13.Etisalat_GitHub_Scripts\\3GPP_2000_12.asn','ber')
encoded = open("E:\\3.Etisalat UAE\\13.Etisalat_GitHub_Scripts\\G20191021.1315-20191021.1330_MS21%3A1004","rb")
content = encoded.read()

##### Converting the Schema Value from Str to bytearray #########
Schema=bytearray()
Schema.extend(content)
##### Decoding the output using the Schema ##########

output=foo.decode('MeasDataCollection', content,check_constraints=False) # output is type(dict)

###### Printing out the output in a txt file ########
for keys in output:
    output_Directory.write(str(keys)+str(output[keys])+" "+"\n")


########## Running time of the Script ##############
Running_time=time.time() - start_time_total
print("Runnning_time is: "+ str(Running_time) +" "+"seconds")

