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


class AbstractHandle(object):

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

    def new_handle(self, context=None):
        """
        The new_handle function returns a Handle object with a url and a
        node id. The new_handle function invokes the localize_handle
        method first to set the url and then invokes the initialize_handle
        function to get an ID.
        :returns: instance of type "Handle" -> structure: parameter "hid" of
           type "HandleId" (Handle provides a unique reference that enables
           access to the data files through functions provided as part of the
           HandleService. In the case of using shock, the id is the node id.
           In the case of using shock the value of type is shock. In the
           future these values should enumerated. The value of url is the
           http address of the shock server, including the protocol (http or
           https) and if necessary the port. The values of remote_md5 and
           remote_sha1 are those computed on the file in the remote data
           store. These can be used to verify uploads and downloads.),
           parameter "file_name" of String, parameter "id" of type "NodeId",
           parameter "type" of String, parameter "url" of String, parameter
           "remote_md5" of String, parameter "remote_sha1" of String
        """
        return self._client.call_method(
            'AbstractHandle.new_handle',
            [], self._service_ver, context)

    def localize_handle(self, h1, service_name, context=None):
        """
        The localize_handle function attempts to locate a shock server near
        the service. The localize_handle function must be called before the
                   Handle is initialized becuase when the handle is initialized, it is
                   given a node id that maps to the shock server where the node was
                   created. This function should not be called directly.
        :param h1: instance of type "Handle" -> structure: parameter "hid" of
           type "HandleId" (Handle provides a unique reference that enables
           access to the data files through functions provided as part of the
           HandleService. In the case of using shock, the id is the node id.
           In the case of using shock the value of type is shock. In the
           future these values should enumerated. The value of url is the
           http address of the shock server, including the protocol (http or
           https) and if necessary the port. The values of remote_md5 and
           remote_sha1 are those computed on the file in the remote data
           store. These can be used to verify uploads and downloads.),
           parameter "file_name" of String, parameter "id" of type "NodeId",
           parameter "type" of String, parameter "url" of String, parameter
           "remote_md5" of String, parameter "remote_sha1" of String
        :param service_name: instance of String
        :returns: instance of type "Handle" -> structure: parameter "hid" of
           type "HandleId" (Handle provides a unique reference that enables
           access to the data files through functions provided as part of the
           HandleService. In the case of using shock, the id is the node id.
           In the case of using shock the value of type is shock. In the
           future these values should enumerated. The value of url is the
           http address of the shock server, including the protocol (http or
           https) and if necessary the port. The values of remote_md5 and
           remote_sha1 are those computed on the file in the remote data
           store. These can be used to verify uploads and downloads.),
           parameter "file_name" of String, parameter "id" of type "NodeId",
           parameter "type" of String, parameter "url" of String, parameter
           "remote_md5" of String, parameter "remote_sha1" of String
        """
        return self._client.call_method(
            'AbstractHandle.localize_handle',
            [h1, service_name], self._service_ver, context)

    def initialize_handle(self, h1, context=None):
        """
        The initialize_handle returns a Handle object with an ID. This
        function should not be called directly
        :param h1: instance of type "Handle" -> structure: parameter "hid" of
           type "HandleId" (Handle provides a unique reference that enables
           access to the data files through functions provided as part of the
           HandleService. In the case of using shock, the id is the node id.
           In the case of using shock the value of type is shock. In the
           future these values should enumerated. The value of url is the
           http address of the shock server, including the protocol (http or
           https) and if necessary the port. The values of remote_md5 and
           remote_sha1 are those computed on the file in the remote data
           store. These can be used to verify uploads and downloads.),
           parameter "file_name" of String, parameter "id" of type "NodeId",
           parameter "type" of String, parameter "url" of String, parameter
           "remote_md5" of String, parameter "remote_sha1" of String
        :returns: instance of type "Handle" -> structure: parameter "hid" of
           type "HandleId" (Handle provides a unique reference that enables
           access to the data files through functions provided as part of the
           HandleService. In the case of using shock, the id is the node id.
           In the case of using shock the value of type is shock. In the
           future these values should enumerated. The value of url is the
           http address of the shock server, including the protocol (http or
           https) and if necessary the port. The values of remote_md5 and
           remote_sha1 are those computed on the file in the remote data
           store. These can be used to verify uploads and downloads.),
           parameter "file_name" of String, parameter "id" of type "NodeId",
           parameter "type" of String, parameter "url" of String, parameter
           "remote_md5" of String, parameter "remote_sha1" of String
        """
        return self._client.call_method(
            'AbstractHandle.initialize_handle',
            [h1], self._service_ver, context)

    def persist_handle(self, h, context=None):
        """
        The persist_handle writes the handle to a persistent store
        that can be later retrieved using the list_handles
        function.
        :param h: instance of type "Handle" -> structure: parameter "hid" of
           type "HandleId" (Handle provides a unique reference that enables
           access to the data files through functions provided as part of the
           HandleService. In the case of using shock, the id is the node id.
           In the case of using shock the value of type is shock. In the
           future these values should enumerated. The value of url is the
           http address of the shock server, including the protocol (http or
           https) and if necessary the port. The values of remote_md5 and
           remote_sha1 are those computed on the file in the remote data
           store. These can be used to verify uploads and downloads.),
           parameter "file_name" of String, parameter "id" of type "NodeId",
           parameter "type" of String, parameter "url" of String, parameter
           "remote_md5" of String, parameter "remote_sha1" of String
        :returns: instance of String
        """
        return self._client.call_method(
            'AbstractHandle.persist_handle',
            [h], self._service_ver, context)

    def upload(self, infile, context=None):
        """
        The upload and download functions  provide an empty
        implementation that must be provided in a client. If a concrete
        implementation is not provided an error is thrown. These are
        the equivelant of abstract methods, with runtime rather than
        compile time inforcement.
                
        [client_implemented]
        :param infile: instance of String
        :returns: instance of type "Handle" -> structure: parameter "hid" of
           type "HandleId" (Handle provides a unique reference that enables
           access to the data files through functions provided as part of the
           HandleService. In the case of using shock, the id is the node id.
           In the case of using shock the value of type is shock. In the
           future these values should enumerated. The value of url is the
           http address of the shock server, including the protocol (http or
           https) and if necessary the port. The values of remote_md5 and
           remote_sha1 are those computed on the file in the remote data
           store. These can be used to verify uploads and downloads.),
           parameter "file_name" of String, parameter "id" of type "NodeId",
           parameter "type" of String, parameter "url" of String, parameter
           "remote_md5" of String, parameter "remote_sha1" of String
        """
        return self._client.call_method(
            'AbstractHandle.upload',
            [infile], self._service_ver, context)

    def download(self, h, outfile, context=None):
        """
        The upload and download functions  provide an empty
        implementation that must be provided in a client. If a concrete
        implementation is not provided an error is thrown. These are
        the equivelant of abstract methods, with runtime rather than
        compile time inforcement.
        [client_implemented]
        :param h: instance of type "Handle" -> structure: parameter "hid" of
           type "HandleId" (Handle provides a unique reference that enables
           access to the data files through functions provided as part of the
           HandleService. In the case of using shock, the id is the node id.
           In the case of using shock the value of type is shock. In the
           future these values should enumerated. The value of url is the
           http address of the shock server, including the protocol (http or
           https) and if necessary the port. The values of remote_md5 and
           remote_sha1 are those computed on the file in the remote data
           store. These can be used to verify uploads and downloads.),
           parameter "file_name" of String, parameter "id" of type "NodeId",
           parameter "type" of String, parameter "url" of String, parameter
           "remote_md5" of String, parameter "remote_sha1" of String
        :param outfile: instance of String
        """
        return self._client.call_method(
            'AbstractHandle.download',
            [h, outfile], self._service_ver, context)

    def upload_metadata(self, h, infile, context=None):
        """
        The upload_metadata function uploads metadata to an existing
        handle. This means that the data that the handle represents
        has already been uploaded. Uploading meta data before the data
        has been uploaded is not currently supported.
        [client_implemented]
        :param h: instance of type "Handle" -> structure: parameter "hid" of
           type "HandleId" (Handle provides a unique reference that enables
           access to the data files through functions provided as part of the
           HandleService. In the case of using shock, the id is the node id.
           In the case of using shock the value of type is shock. In the
           future these values should enumerated. The value of url is the
           http address of the shock server, including the protocol (http or
           https) and if necessary the port. The values of remote_md5 and
           remote_sha1 are those computed on the file in the remote data
           store. These can be used to verify uploads and downloads.),
           parameter "file_name" of String, parameter "id" of type "NodeId",
           parameter "type" of String, parameter "url" of String, parameter
           "remote_md5" of String, parameter "remote_sha1" of String
        :param infile: instance of String
        """
        return self._client.call_method(
            'AbstractHandle.upload_metadata',
            [h, infile], self._service_ver, context)

    def download_metadata(self, h, outfile, context=None):
        """
        The download_metadata function downloads metadata associated
        with the data handle and writes it to a file.
        [client_implemented]
        :param h: instance of type "Handle" -> structure: parameter "hid" of
           type "HandleId" (Handle provides a unique reference that enables
           access to the data files through functions provided as part of the
           HandleService. In the case of using shock, the id is the node id.
           In the case of using shock the value of type is shock. In the
           future these values should enumerated. The value of url is the
           http address of the shock server, including the protocol (http or
           https) and if necessary the port. The values of remote_md5 and
           remote_sha1 are those computed on the file in the remote data
           store. These can be used to verify uploads and downloads.),
           parameter "file_name" of String, parameter "id" of type "NodeId",
           parameter "type" of String, parameter "url" of String, parameter
           "remote_md5" of String, parameter "remote_sha1" of String
        :param outfile: instance of String
        """
        return self._client.call_method(
            'AbstractHandle.download_metadata',
            [h, outfile], self._service_ver, context)

    def hids_to_handles(self, hids, context=None):
        """
        Given a list of handle ids, this function returns
        a list of handles.
        :param hids: instance of list of type "HandleId" (Handle provides a
           unique reference that enables access to the data files through
           functions provided as part of the HandleService. In the case of
           using shock, the id is the node id. In the case of using shock the
           value of type is shock. In the future these values should
           enumerated. The value of url is the http address of the shock
           server, including the protocol (http or https) and if necessary
           the port. The values of remote_md5 and remote_sha1 are those
           computed on the file in the remote data store. These can be used
           to verify uploads and downloads.)
        :returns: instance of list of type "Handle" -> structure: parameter
           "hid" of type "HandleId" (Handle provides a unique reference that
           enables access to the data files through functions provided as
           part of the HandleService. In the case of using shock, the id is
           the node id. In the case of using shock the value of type is
           shock. In the future these values should enumerated. The value of
           url is the http address of the shock server, including the
           protocol (http or https) and if necessary the port. The values of
           remote_md5 and remote_sha1 are those computed on the file in the
           remote data store. These can be used to verify uploads and
           downloads.), parameter "file_name" of String, parameter "id" of
           type "NodeId", parameter "type" of String, parameter "url" of
           String, parameter "remote_md5" of String, parameter "remote_sha1"
           of String
        """
        return self._client.call_method(
            'AbstractHandle.hids_to_handles',
            [hids], self._service_ver, context)

    def are_readable(self, arg_1, context=None):
        """
        Given a list of handle ids, this function determines if
        the underlying data is readable by the caller. If any
        one of the handle ids reference unreadable data this
        function returns false.
        :param arg_1: instance of list of type "HandleId" (Handle provides a
           unique reference that enables access to the data files through
           functions provided as part of the HandleService. In the case of
           using shock, the id is the node id. In the case of using shock the
           value of type is shock. In the future these values should
           enumerated. The value of url is the http address of the shock
           server, including the protocol (http or https) and if necessary
           the port. The values of remote_md5 and remote_sha1 are those
           computed on the file in the remote data store. These can be used
           to verify uploads and downloads.)
        :returns: instance of Long
        """
        return self._client.call_method(
            'AbstractHandle.are_readable',
            [arg_1], self._service_ver, context)

    def is_owner(self, arg_1, context=None):
        """
        Given a list of handle ids, this function determines if the underlying
        data is owned by the caller. If any one of the handle ids reference
        unreadable data this function returns false.
        :param arg_1: instance of list of type "HandleId" (Handle provides a
           unique reference that enables access to the data files through
           functions provided as part of the HandleService. In the case of
           using shock, the id is the node id. In the case of using shock the
           value of type is shock. In the future these values should
           enumerated. The value of url is the http address of the shock
           server, including the protocol (http or https) and if necessary
           the port. The values of remote_md5 and remote_sha1 are those
           computed on the file in the remote data store. These can be used
           to verify uploads and downloads.)
        :returns: instance of Long
        """
        return self._client.call_method(
            'AbstractHandle.is_owner',
            [arg_1], self._service_ver, context)

    def is_readable(self, id, context=None):
        """
        Given a handle id, this function queries the underlying
        data store to see if the data being referred to is
        readable to by the caller.
        :param id: instance of String
        :returns: instance of Long
        """
        return self._client.call_method(
            'AbstractHandle.is_readable',
            [id], self._service_ver, context)

    def list_handles(self, context=None):
        """
        The list function returns the set of handles that were
        created by the user.
        :returns: instance of list of type "Handle" -> structure: parameter
           "hid" of type "HandleId" (Handle provides a unique reference that
           enables access to the data files through functions provided as
           part of the HandleService. In the case of using shock, the id is
           the node id. In the case of using shock the value of type is
           shock. In the future these values should enumerated. The value of
           url is the http address of the shock server, including the
           protocol (http or https) and if necessary the port. The values of
           remote_md5 and remote_sha1 are those computed on the file in the
           remote data store. These can be used to verify uploads and
           downloads.), parameter "file_name" of String, parameter "id" of
           type "NodeId", parameter "type" of String, parameter "url" of
           String, parameter "remote_md5" of String, parameter "remote_sha1"
           of String
        """
        return self._client.call_method(
            'AbstractHandle.list_handles',
            [], self._service_ver, context)

    def delete_handles(self, l, context=None):
        """
        The delete_handles function takes a list of handles
        and deletes them on the handle service server.
        :param l: instance of list of type "Handle" -> structure: parameter
           "hid" of type "HandleId" (Handle provides a unique reference that
           enables access to the data files through functions provided as
           part of the HandleService. In the case of using shock, the id is
           the node id. In the case of using shock the value of type is
           shock. In the future these values should enumerated. The value of
           url is the http address of the shock server, including the
           protocol (http or https) and if necessary the port. The values of
           remote_md5 and remote_sha1 are those computed on the file in the
           remote data store. These can be used to verify uploads and
           downloads.), parameter "file_name" of String, parameter "id" of
           type "NodeId", parameter "type" of String, parameter "url" of
           String, parameter "remote_md5" of String, parameter "remote_sha1"
           of String
        """
        return self._client.call_method(
            'AbstractHandle.delete_handles',
            [l], self._service_ver, context)

    def give(self, user, perm, h, context=None):
        """
        :param user: instance of String
        :param perm: instance of String
        :param h: instance of type "Handle" -> structure: parameter "hid" of
           type "HandleId" (Handle provides a unique reference that enables
           access to the data files through functions provided as part of the
           HandleService. In the case of using shock, the id is the node id.
           In the case of using shock the value of type is shock. In the
           future these values should enumerated. The value of url is the
           http address of the shock server, including the protocol (http or
           https) and if necessary the port. The values of remote_md5 and
           remote_sha1 are those computed on the file in the remote data
           store. These can be used to verify uploads and downloads.),
           parameter "file_name" of String, parameter "id" of type "NodeId",
           parameter "type" of String, parameter "url" of String, parameter
           "remote_md5" of String, parameter "remote_sha1" of String
        """
        return self._client.call_method(
            'AbstractHandle.give',
            [user, perm, h], self._service_ver, context)

    def ids_to_handles(self, ids, context=None):
        """
        Given a list of ids, this function returns
        a list of handles. In case of Shock, the list of ids
        are shock node ids and this function the handles, which
        contains Shock url and related information.
        :param ids: instance of list of type "NodeId"
        :returns: instance of list of type "Handle" -> structure: parameter
           "hid" of type "HandleId" (Handle provides a unique reference that
           enables access to the data files through functions provided as
           part of the HandleService. In the case of using shock, the id is
           the node id. In the case of using shock the value of type is
           shock. In the future these values should enumerated. The value of
           url is the http address of the shock server, including the
           protocol (http or https) and if necessary the port. The values of
           remote_md5 and remote_sha1 are those computed on the file in the
           remote data store. These can be used to verify uploads and
           downloads.), parameter "file_name" of String, parameter "id" of
           type "NodeId", parameter "type" of String, parameter "url" of
           String, parameter "remote_md5" of String, parameter "remote_sha1"
           of String
        """
        return self._client.call_method(
            'AbstractHandle.ids_to_handles',
            [ids], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('AbstractHandle.status',
                                        [], self._service_ver, context)
