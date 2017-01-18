# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_quast(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def run_QUAST_app(self, params, context=None):
        """
        Run QUAST and save a KBaseReport with the output.
        :param params: instance of type "QUASTParams" (Input for running
           QUAST. assemblies - the list of assemblies upon which QUAST will
           be run. -OR- files - the list of FASTA files upon which QUAST will
           be run.) -> structure: parameter "assemblies" of list of type
           "assembly_ref" (An X/Y/Z style reference to a workspace object
           containing an assembly, either a KBaseGenomes.ContigSet or
           KBaseGenomeAnnotations.Assembly.), parameter "files" of list of
           type "FASTAFile" (A local FASTA file. path - the path to the FASTA
           file. label - the label to use for the file in the QUAST output.)
           -> structure: parameter "path" of String, parameter "label" of
           String
        :returns: instance of type "QUASTAppOutput" (Output of the
           run_quast_app function. report_name - the name of the
           KBaseReport.Report workspace object. report_ref - the workspace
           reference of the report.) -> structure: parameter "report_name" of
           String, parameter "report_ref" of String
        """
        return self._client.call_method(
            'kb_quast.run_QUAST_app',
            [params], self._service_ver, context)

    def run_QUAST(self, params, context=None):
        """
        Run QUAST and return a shock node containing the zipped QUAST output.
        :param params: instance of type "QUASTParams" (Input for running
           QUAST. assemblies - the list of assemblies upon which QUAST will
           be run. -OR- files - the list of FASTA files upon which QUAST will
           be run.) -> structure: parameter "assemblies" of list of type
           "assembly_ref" (An X/Y/Z style reference to a workspace object
           containing an assembly, either a KBaseGenomes.ContigSet or
           KBaseGenomeAnnotations.Assembly.), parameter "files" of list of
           type "FASTAFile" (A local FASTA file. path - the path to the FASTA
           file. label - the label to use for the file in the QUAST output.)
           -> structure: parameter "path" of String, parameter "label" of
           String
        :returns: instance of type "QUASTOutput" (Ouput of the run_quast
           function. shock_id - the id of the shock node where the zipped
           QUAST output is stored. handle - the new handle for the shock
           node. node_file_name - the name of the file stored in Shock. size
           - the size of the file stored in shock.) -> structure: parameter
           "shock_id" of String, parameter "handle" of type "Handle" (A
           handle for a file stored in Shock. hid - the id of the handle in
           the Handle Service that references this shock node id - the id for
           the shock node url - the url of the shock server type - the type
           of the handle. This should always be shock. file_name - the name
           of the file remote_md5 - the md5 digest of the file.) ->
           structure: parameter "hid" of String, parameter "file_name" of
           String, parameter "id" of String, parameter "url" of String,
           parameter "type" of String, parameter "remote_md5" of String,
           parameter "node_file_name" of String, parameter "size" of String
        """
        return self._client.call_method(
            'kb_quast.run_QUAST',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_quast.status',
                                        [], self._service_ver, context)