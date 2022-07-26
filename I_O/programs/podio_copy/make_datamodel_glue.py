#!/usr/bin/env python
#
# Copyright 2022, David Lawrence
# Subject to the terms in the LICENSE file found in the top-level directory.
#
#

#
#  This is a stop gap and not intended for long term.  2022-07-09  DL
#
# This will scan the list of files in the EDM4hep datamodel directory
# (pointed to by the EDM4HEP_ROOT environment variable). Using the
# filenames, it will generate some C++ code that can be used by
# the JEventSourcePODIO and EDM4hepWriter classes to read and write all
# of those types.

import os
import sys
import glob

print('Generating datamodel_glue.h ...')

EDM4HEP_ROOT = os.environ.get("EDM4HEP_ROOT")
collectionfiles = glob.glob(EDM4HEP_ROOT+'/include/edm4hep/*Collection.h')
header_lines = []
get_code_lines = []
put_code_lines = []
for f in collectionfiles:
    header_fname = f.split('/edm4hep')[-1]
    basename = header_fname.split('/')[-1].split('Collection.h')[0]
    header = '#include <edm4hep' + header_fname + '>'
    header_lines += [header]

    code1 = '    if( colltype=="edm4hep::'+basename+'" ) return CopyCollectionT<edm4hep::'+basename+', edm4hep::'+basename+'Collection>( store_in, store_out, name);'
    put_code_lines += [code1]



put_code_lines += ['    return nullptr;']

with open('datamodel_glue.h', 'w') as f:
    f.write('\n// This file automatically generated by the make_datamodel.py script\n')
    f.write('#include <podio/EventStore.h>\n')
    f.write('\n'.join(header_lines))
    f.write('\n\ntemplate<typename T, typename C>\n')
    f.write('podio::CollectionBase* CopyCollectionT(podio::EventStore& store_in, podio::EventStore& store_out, const std::string& name);\n')
    f.write('\npodio::CollectionBase* CopyCollection(podio::EventStore& store_in, podio::EventStore& store_out, const std::string& name, const std::string &colltype){\n')
    f.write('\n'.join(put_code_lines))
    f.write('\n}\n')
    f.close()
