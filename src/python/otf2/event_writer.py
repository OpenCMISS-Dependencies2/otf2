# Generated by OTF2 Template Engine

import _otf2

from . import events


def _generate_doc_from(event):
    def decorator(func):
        doc_str = "Writes a new :py:class:`otf2.events.{}` event to the corresponding location of \
                  the writer.\n".format(event.__name__)
        doc_str += "\n"

        for name, type, desc in event._fields:
            if type.endswith("Ref"):
                type = "otf2.definitions.{}".format(type[:-3])
            elif "int" in type:
                type = "int"
            elif type.startswith("dict"):
                pass
            elif type.startswith("array"):
                pass
            else:
                type = "otf2.{}".format(type)
            doc_str += ":param {type} {name}: {desc}\n".format(name=name, type=type, desc=desc)
        func.__doc__ = doc_str
        return func
    return decorator


class EventWriter(object):
    def __init__(self, archive, location):
        assert archive
        assert location
        self._archive = archive
        self._location = location

        # Not used yet, but to prevent false errors, when reading
        self._def_handle = _otf2.Archive_GetDefWriter(archive._handle, location._ref)

        self._handle = _otf2.Archive_GetEvtWriter(archive._handle, location._ref)

        location._number_of_events_written = 0

    def close(self):
        _otf2.Archive_CloseDefWriter(self._archive._handle, self._def_handle)
        _otf2.Archive_CloseEvtWriter(self._archive._handle, self._handle)

    def write(self, event):
        """
            Writes a given event to the corresponding location

            :param event: :py:class:`otf2.events._Event`
        """
        self._archive._update_timestamps(event.time)
        self._location._number_of_events_written += 1
        event._write(self)

    @property
    def handle(self):
        """
            Gives access to the underlaying OTF2 event writer
        """
        return self._handle

    def __call__(self, event):
        self.write(event)

    @_generate_doc_from(events.BufferFlush)
    def buffer_flush(self, time, *args, **kwargs):
        self.write(events.BufferFlush(time, *args, **kwargs))

    @_generate_doc_from(events.MeasurementOnOff)
    def measurement_on_off(self, time, *args, **kwargs):
        self.write(events.MeasurementOnOff(time, *args, **kwargs))

    @_generate_doc_from(events.Enter)
    def enter(self, time, *args, **kwargs):
        self.write(events.Enter(time, *args, **kwargs))

    @_generate_doc_from(events.Leave)
    def leave(self, time, *args, **kwargs):
        self.write(events.Leave(time, *args, **kwargs))

    @_generate_doc_from(events.MpiSend)
    def mpi_send(self, time, *args, **kwargs):
        self.write(events.MpiSend(time, *args, **kwargs))

    @_generate_doc_from(events.MpiIsend)
    def mpi_isend(self, time, *args, **kwargs):
        self.write(events.MpiIsend(time, *args, **kwargs))

    @_generate_doc_from(events.MpiIsendComplete)
    def mpi_isend_complete(self, time, *args, **kwargs):
        self.write(events.MpiIsendComplete(time, *args, **kwargs))

    @_generate_doc_from(events.MpiIrecvRequest)
    def mpi_irecv_request(self, time, *args, **kwargs):
        self.write(events.MpiIrecvRequest(time, *args, **kwargs))

    @_generate_doc_from(events.MpiRecv)
    def mpi_recv(self, time, *args, **kwargs):
        self.write(events.MpiRecv(time, *args, **kwargs))

    @_generate_doc_from(events.MpiIrecv)
    def mpi_irecv(self, time, *args, **kwargs):
        self.write(events.MpiIrecv(time, *args, **kwargs))

    @_generate_doc_from(events.MpiRequestTest)
    def mpi_request_test(self, time, *args, **kwargs):
        self.write(events.MpiRequestTest(time, *args, **kwargs))

    @_generate_doc_from(events.MpiRequestCancelled)
    def mpi_request_cancelled(self, time, *args, **kwargs):
        self.write(events.MpiRequestCancelled(time, *args, **kwargs))

    @_generate_doc_from(events.MpiCollectiveBegin)
    def mpi_collective_begin(self, time, *args, **kwargs):
        self.write(events.MpiCollectiveBegin(time, *args, **kwargs))

    @_generate_doc_from(events.MpiCollectiveEnd)
    def mpi_collective_end(self, time, *args, **kwargs):
        self.write(events.MpiCollectiveEnd(time, *args, **kwargs))

    @_generate_doc_from(events.OmpFork)
    def omp_fork(self, time, *args, **kwargs):
        self.write(events.OmpFork(time, *args, **kwargs))

    @_generate_doc_from(events.OmpJoin)
    def omp_join(self, time, *args, **kwargs):
        self.write(events.OmpJoin(time, *args, **kwargs))

    @_generate_doc_from(events.OmpAcquireLock)
    def omp_acquire_lock(self, time, *args, **kwargs):
        self.write(events.OmpAcquireLock(time, *args, **kwargs))

    @_generate_doc_from(events.OmpReleaseLock)
    def omp_release_lock(self, time, *args, **kwargs):
        self.write(events.OmpReleaseLock(time, *args, **kwargs))

    @_generate_doc_from(events.OmpTaskCreate)
    def omp_task_create(self, time, *args, **kwargs):
        self.write(events.OmpTaskCreate(time, *args, **kwargs))

    @_generate_doc_from(events.OmpTaskSwitch)
    def omp_task_switch(self, time, *args, **kwargs):
        self.write(events.OmpTaskSwitch(time, *args, **kwargs))

    @_generate_doc_from(events.OmpTaskComplete)
    def omp_task_complete(self, time, *args, **kwargs):
        self.write(events.OmpTaskComplete(time, *args, **kwargs))

    @_generate_doc_from(events.Metric)
    def metric(self, time, *args, **kwargs):
        self.write(events.Metric(time, *args, **kwargs))

    @_generate_doc_from(events.ParameterString)
    def parameter_string(self, time, *args, **kwargs):
        self.write(events.ParameterString(time, *args, **kwargs))

    @_generate_doc_from(events.ParameterInt)
    def parameter_int(self, time, *args, **kwargs):
        self.write(events.ParameterInt(time, *args, **kwargs))

    @_generate_doc_from(events.ParameterUnsignedInt)
    def parameter_unsigned_int(self, time, *args, **kwargs):
        self.write(events.ParameterUnsignedInt(time, *args, **kwargs))

    @_generate_doc_from(events.RmaWinCreate)
    def rma_win_create(self, time, *args, **kwargs):
        self.write(events.RmaWinCreate(time, *args, **kwargs))

    @_generate_doc_from(events.RmaWinDestroy)
    def rma_win_destroy(self, time, *args, **kwargs):
        self.write(events.RmaWinDestroy(time, *args, **kwargs))

    @_generate_doc_from(events.RmaCollectiveBegin)
    def rma_collective_begin(self, time, *args, **kwargs):
        self.write(events.RmaCollectiveBegin(time, *args, **kwargs))

    @_generate_doc_from(events.RmaCollectiveEnd)
    def rma_collective_end(self, time, *args, **kwargs):
        self.write(events.RmaCollectiveEnd(time, *args, **kwargs))

    @_generate_doc_from(events.RmaGroupSync)
    def rma_group_sync(self, time, *args, **kwargs):
        self.write(events.RmaGroupSync(time, *args, **kwargs))

    @_generate_doc_from(events.RmaRequestLock)
    def rma_request_lock(self, time, *args, **kwargs):
        self.write(events.RmaRequestLock(time, *args, **kwargs))

    @_generate_doc_from(events.RmaAcquireLock)
    def rma_acquire_lock(self, time, *args, **kwargs):
        self.write(events.RmaAcquireLock(time, *args, **kwargs))

    @_generate_doc_from(events.RmaTryLock)
    def rma_try_lock(self, time, *args, **kwargs):
        self.write(events.RmaTryLock(time, *args, **kwargs))

    @_generate_doc_from(events.RmaReleaseLock)
    def rma_release_lock(self, time, *args, **kwargs):
        self.write(events.RmaReleaseLock(time, *args, **kwargs))

    @_generate_doc_from(events.RmaSync)
    def rma_sync(self, time, *args, **kwargs):
        self.write(events.RmaSync(time, *args, **kwargs))

    @_generate_doc_from(events.RmaWaitChange)
    def rma_wait_change(self, time, *args, **kwargs):
        self.write(events.RmaWaitChange(time, *args, **kwargs))

    @_generate_doc_from(events.RmaPut)
    def rma_put(self, time, *args, **kwargs):
        self.write(events.RmaPut(time, *args, **kwargs))

    @_generate_doc_from(events.RmaGet)
    def rma_get(self, time, *args, **kwargs):
        self.write(events.RmaGet(time, *args, **kwargs))

    @_generate_doc_from(events.RmaAtomic)
    def rma_atomic(self, time, *args, **kwargs):
        self.write(events.RmaAtomic(time, *args, **kwargs))

    @_generate_doc_from(events.RmaOpCompleteBlocking)
    def rma_op_complete_blocking(self, time, *args, **kwargs):
        self.write(events.RmaOpCompleteBlocking(time, *args, **kwargs))

    @_generate_doc_from(events.RmaOpCompleteNonBlocking)
    def rma_op_complete_non_blocking(self, time, *args, **kwargs):
        self.write(events.RmaOpCompleteNonBlocking(time, *args, **kwargs))

    @_generate_doc_from(events.RmaOpTest)
    def rma_op_test(self, time, *args, **kwargs):
        self.write(events.RmaOpTest(time, *args, **kwargs))

    @_generate_doc_from(events.RmaOpCompleteRemote)
    def rma_op_complete_remote(self, time, *args, **kwargs):
        self.write(events.RmaOpCompleteRemote(time, *args, **kwargs))

    @_generate_doc_from(events.ThreadFork)
    def thread_fork(self, time, *args, **kwargs):
        self.write(events.ThreadFork(time, *args, **kwargs))

    @_generate_doc_from(events.ThreadJoin)
    def thread_join(self, time, *args, **kwargs):
        self.write(events.ThreadJoin(time, *args, **kwargs))

    @_generate_doc_from(events.ThreadTeamBegin)
    def thread_team_begin(self, time, *args, **kwargs):
        self.write(events.ThreadTeamBegin(time, *args, **kwargs))

    @_generate_doc_from(events.ThreadTeamEnd)
    def thread_team_end(self, time, *args, **kwargs):
        self.write(events.ThreadTeamEnd(time, *args, **kwargs))

    @_generate_doc_from(events.ThreadAcquireLock)
    def thread_acquire_lock(self, time, *args, **kwargs):
        self.write(events.ThreadAcquireLock(time, *args, **kwargs))

    @_generate_doc_from(events.ThreadReleaseLock)
    def thread_release_lock(self, time, *args, **kwargs):
        self.write(events.ThreadReleaseLock(time, *args, **kwargs))

    @_generate_doc_from(events.ThreadTaskCreate)
    def thread_task_create(self, time, *args, **kwargs):
        self.write(events.ThreadTaskCreate(time, *args, **kwargs))

    @_generate_doc_from(events.ThreadTaskSwitch)
    def thread_task_switch(self, time, *args, **kwargs):
        self.write(events.ThreadTaskSwitch(time, *args, **kwargs))

    @_generate_doc_from(events.ThreadTaskComplete)
    def thread_task_complete(self, time, *args, **kwargs):
        self.write(events.ThreadTaskComplete(time, *args, **kwargs))

    @_generate_doc_from(events.ThreadCreate)
    def thread_create(self, time, *args, **kwargs):
        self.write(events.ThreadCreate(time, *args, **kwargs))

    @_generate_doc_from(events.ThreadBegin)
    def thread_begin(self, time, *args, **kwargs):
        self.write(events.ThreadBegin(time, *args, **kwargs))

    @_generate_doc_from(events.ThreadWait)
    def thread_wait(self, time, *args, **kwargs):
        self.write(events.ThreadWait(time, *args, **kwargs))

    @_generate_doc_from(events.ThreadEnd)
    def thread_end(self, time, *args, **kwargs):
        self.write(events.ThreadEnd(time, *args, **kwargs))

    @_generate_doc_from(events.CallingContextEnter)
    def calling_context_enter(self, time, *args, **kwargs):
        self.write(events.CallingContextEnter(time, *args, **kwargs))

    @_generate_doc_from(events.CallingContextLeave)
    def calling_context_leave(self, time, *args, **kwargs):
        self.write(events.CallingContextLeave(time, *args, **kwargs))

    @_generate_doc_from(events.CallingContextSample)
    def calling_context_sample(self, time, *args, **kwargs):
        self.write(events.CallingContextSample(time, *args, **kwargs))

    @_generate_doc_from(events.IoCreateHandle)
    def io_create_handle(self, time, *args, **kwargs):
        self.write(events.IoCreateHandle(time, *args, **kwargs))

    @_generate_doc_from(events.IoDestroyHandle)
    def io_destroy_handle(self, time, *args, **kwargs):
        self.write(events.IoDestroyHandle(time, *args, **kwargs))

    @_generate_doc_from(events.IoDuplicateHandle)
    def io_duplicate_handle(self, time, *args, **kwargs):
        self.write(events.IoDuplicateHandle(time, *args, **kwargs))

    @_generate_doc_from(events.IoSeek)
    def io_seek(self, time, *args, **kwargs):
        self.write(events.IoSeek(time, *args, **kwargs))

    @_generate_doc_from(events.IoChangeStatusFlags)
    def io_change_status_flags(self, time, *args, **kwargs):
        self.write(events.IoChangeStatusFlags(time, *args, **kwargs))

    @_generate_doc_from(events.IoDeleteFile)
    def io_delete_file(self, time, *args, **kwargs):
        self.write(events.IoDeleteFile(time, *args, **kwargs))

    @_generate_doc_from(events.IoOperationBegin)
    def io_operation_begin(self, time, *args, **kwargs):
        self.write(events.IoOperationBegin(time, *args, **kwargs))

    @_generate_doc_from(events.IoOperationTest)
    def io_operation_test(self, time, *args, **kwargs):
        self.write(events.IoOperationTest(time, *args, **kwargs))

    @_generate_doc_from(events.IoOperationIssued)
    def io_operation_issued(self, time, *args, **kwargs):
        self.write(events.IoOperationIssued(time, *args, **kwargs))

    @_generate_doc_from(events.IoOperationComplete)
    def io_operation_complete(self, time, *args, **kwargs):
        self.write(events.IoOperationComplete(time, *args, **kwargs))

    @_generate_doc_from(events.IoOperationCancelled)
    def io_operation_cancelled(self, time, *args, **kwargs):
        self.write(events.IoOperationCancelled(time, *args, **kwargs))

    @_generate_doc_from(events.IoAcquireLock)
    def io_acquire_lock(self, time, *args, **kwargs):
        self.write(events.IoAcquireLock(time, *args, **kwargs))

    @_generate_doc_from(events.IoReleaseLock)
    def io_release_lock(self, time, *args, **kwargs):
        self.write(events.IoReleaseLock(time, *args, **kwargs))

    @_generate_doc_from(events.IoTryLock)
    def io_try_lock(self, time, *args, **kwargs):
        self.write(events.IoTryLock(time, *args, **kwargs))

    @_generate_doc_from(events.ProgramBegin)
    def program_begin(self, time, *args, **kwargs):
        self.write(events.ProgramBegin(time, *args, **kwargs))

    @_generate_doc_from(events.ProgramEnd)
    def program_end(self, time, *args, **kwargs):
        self.write(events.ProgramEnd(time, *args, **kwargs))

    @_generate_doc_from(events.NonBlockingCollectiveRequest)
    def non_blocking_collective_request(self, time, *args, **kwargs):
        self.write(events.NonBlockingCollectiveRequest(time, *args, **kwargs))

    @_generate_doc_from(events.NonBlockingCollectiveComplete)
    def non_blocking_collective_complete(self, time, *args, **kwargs):
        self.write(events.NonBlockingCollectiveComplete(time, *args, **kwargs))

    @_generate_doc_from(events.CommCreate)
    def comm_create(self, time, *args, **kwargs):
        self.write(events.CommCreate(time, *args, **kwargs))

    @_generate_doc_from(events.CommDestroy)
    def comm_destroy(self, time, *args, **kwargs):
        self.write(events.CommDestroy(time, *args, **kwargs))

    def _buffer_flush(self, attribute_list, time, stop_time):
        _otf2.EvtWriter_BufferFlush(self._handle, attribute_list, time, stop_time)

    def _measurement_on_off(self, attribute_list, time, measurement_mode):
        _otf2.EvtWriter_MeasurementOnOff(self._handle, attribute_list, time, measurement_mode)

    def _enter(self, attribute_list, time, region):
        _otf2.EvtWriter_Enter(self._handle, attribute_list, time, region)

    def _leave(self, attribute_list, time, region):
        _otf2.EvtWriter_Leave(self._handle, attribute_list, time, region)

    def _mpi_send(self, attribute_list, time, receiver, communicator, msg_tag, msg_length):
        _otf2.EvtWriter_MpiSend(self._handle, attribute_list, time, receiver, communicator, msg_tag, msg_length)

    def _mpi_isend(self, attribute_list, time, receiver, communicator, msg_tag, msg_length, request_id):
        _otf2.EvtWriter_MpiIsend(self._handle, attribute_list, time, receiver, communicator, msg_tag, msg_length, request_id)

    def _mpi_isend_complete(self, attribute_list, time, request_id):
        _otf2.EvtWriter_MpiIsendComplete(self._handle, attribute_list, time, request_id)

    def _mpi_irecv_request(self, attribute_list, time, request_id):
        _otf2.EvtWriter_MpiIrecvRequest(self._handle, attribute_list, time, request_id)

    def _mpi_recv(self, attribute_list, time, sender, communicator, msg_tag, msg_length):
        _otf2.EvtWriter_MpiRecv(self._handle, attribute_list, time, sender, communicator, msg_tag, msg_length)

    def _mpi_irecv(self, attribute_list, time, sender, communicator, msg_tag, msg_length, request_id):
        _otf2.EvtWriter_MpiIrecv(self._handle, attribute_list, time, sender, communicator, msg_tag, msg_length, request_id)

    def _mpi_request_test(self, attribute_list, time, request_id):
        _otf2.EvtWriter_MpiRequestTest(self._handle, attribute_list, time, request_id)

    def _mpi_request_cancelled(self, attribute_list, time, request_id):
        _otf2.EvtWriter_MpiRequestCancelled(self._handle, attribute_list, time, request_id)

    def _mpi_collective_begin(self, attribute_list, time):
        _otf2.EvtWriter_MpiCollectiveBegin(self._handle, attribute_list, time)

    def _mpi_collective_end(self, attribute_list, time, collective_op, communicator, root, size_sent, size_received):
        _otf2.EvtWriter_MpiCollectiveEnd(self._handle, attribute_list, time, collective_op, communicator, root, size_sent, size_received)

    def _omp_fork(self, attribute_list, time, number_of_requested_threads):
        _otf2.EvtWriter_OmpFork(self._handle, attribute_list, time, number_of_requested_threads)

    def _omp_join(self, attribute_list, time):
        _otf2.EvtWriter_OmpJoin(self._handle, attribute_list, time)

    def _omp_acquire_lock(self, attribute_list, time, lock_id, acquisition_order):
        _otf2.EvtWriter_OmpAcquireLock(self._handle, attribute_list, time, lock_id, acquisition_order)

    def _omp_release_lock(self, attribute_list, time, lock_id, acquisition_order):
        _otf2.EvtWriter_OmpReleaseLock(self._handle, attribute_list, time, lock_id, acquisition_order)

    def _omp_task_create(self, attribute_list, time, task_id):
        _otf2.EvtWriter_OmpTaskCreate(self._handle, attribute_list, time, task_id)

    def _omp_task_switch(self, attribute_list, time, task_id):
        _otf2.EvtWriter_OmpTaskSwitch(self._handle, attribute_list, time, task_id)

    def _omp_task_complete(self, attribute_list, time, task_id):
        _otf2.EvtWriter_OmpTaskComplete(self._handle, attribute_list, time, task_id)

    def _metric(self, attribute_list, time, metric, type_ids, metric_values):
        _otf2.EvtWriter_Metric(self._handle, attribute_list, time, metric, type_ids, metric_values)

    def _parameter_string(self, attribute_list, time, parameter, string):
        _otf2.EvtWriter_ParameterString(self._handle, attribute_list, time, parameter, string)

    def _parameter_int(self, attribute_list, time, parameter, value):
        _otf2.EvtWriter_ParameterInt(self._handle, attribute_list, time, parameter, value)

    def _parameter_unsigned_int(self, attribute_list, time, parameter, value):
        _otf2.EvtWriter_ParameterUnsignedInt(self._handle, attribute_list, time, parameter, value)

    def _rma_win_create(self, attribute_list, time, win):
        _otf2.EvtWriter_RmaWinCreate(self._handle, attribute_list, time, win)

    def _rma_win_destroy(self, attribute_list, time, win):
        _otf2.EvtWriter_RmaWinDestroy(self._handle, attribute_list, time, win)

    def _rma_collective_begin(self, attribute_list, time):
        _otf2.EvtWriter_RmaCollectiveBegin(self._handle, attribute_list, time)

    def _rma_collective_end(self, attribute_list, time, collective_op, sync_level, win, root, bytes_sent, bytes_received):
        _otf2.EvtWriter_RmaCollectiveEnd(self._handle, attribute_list, time, collective_op, sync_level, win, root, bytes_sent, bytes_received)

    def _rma_group_sync(self, attribute_list, time, sync_level, win, group):
        _otf2.EvtWriter_RmaGroupSync(self._handle, attribute_list, time, sync_level, win, group)

    def _rma_request_lock(self, attribute_list, time, win, remote, lock_id, lock_type):
        _otf2.EvtWriter_RmaRequestLock(self._handle, attribute_list, time, win, remote, lock_id, lock_type)

    def _rma_acquire_lock(self, attribute_list, time, win, remote, lock_id, lock_type):
        _otf2.EvtWriter_RmaAcquireLock(self._handle, attribute_list, time, win, remote, lock_id, lock_type)

    def _rma_try_lock(self, attribute_list, time, win, remote, lock_id, lock_type):
        _otf2.EvtWriter_RmaTryLock(self._handle, attribute_list, time, win, remote, lock_id, lock_type)

    def _rma_release_lock(self, attribute_list, time, win, remote, lock_id):
        _otf2.EvtWriter_RmaReleaseLock(self._handle, attribute_list, time, win, remote, lock_id)

    def _rma_sync(self, attribute_list, time, win, remote, sync_type):
        _otf2.EvtWriter_RmaSync(self._handle, attribute_list, time, win, remote, sync_type)

    def _rma_wait_change(self, attribute_list, time, win):
        _otf2.EvtWriter_RmaWaitChange(self._handle, attribute_list, time, win)

    def _rma_put(self, attribute_list, time, win, remote, bytes, matching_id):
        _otf2.EvtWriter_RmaPut(self._handle, attribute_list, time, win, remote, bytes, matching_id)

    def _rma_get(self, attribute_list, time, win, remote, bytes, matching_id):
        _otf2.EvtWriter_RmaGet(self._handle, attribute_list, time, win, remote, bytes, matching_id)

    def _rma_atomic(self, attribute_list, time, win, remote, type, bytes_sent, bytes_received, matching_id):
        _otf2.EvtWriter_RmaAtomic(self._handle, attribute_list, time, win, remote, type, bytes_sent, bytes_received, matching_id)

    def _rma_op_complete_blocking(self, attribute_list, time, win, matching_id):
        _otf2.EvtWriter_RmaOpCompleteBlocking(self._handle, attribute_list, time, win, matching_id)

    def _rma_op_complete_non_blocking(self, attribute_list, time, win, matching_id):
        _otf2.EvtWriter_RmaOpCompleteNonBlocking(self._handle, attribute_list, time, win, matching_id)

    def _rma_op_test(self, attribute_list, time, win, matching_id):
        _otf2.EvtWriter_RmaOpTest(self._handle, attribute_list, time, win, matching_id)

    def _rma_op_complete_remote(self, attribute_list, time, win, matching_id):
        _otf2.EvtWriter_RmaOpCompleteRemote(self._handle, attribute_list, time, win, matching_id)

    def _thread_fork(self, attribute_list, time, model, number_of_requested_threads):
        _otf2.EvtWriter_ThreadFork(self._handle, attribute_list, time, model, number_of_requested_threads)

    def _thread_join(self, attribute_list, time, model):
        _otf2.EvtWriter_ThreadJoin(self._handle, attribute_list, time, model)

    def _thread_team_begin(self, attribute_list, time, thread_team):
        _otf2.EvtWriter_ThreadTeamBegin(self._handle, attribute_list, time, thread_team)

    def _thread_team_end(self, attribute_list, time, thread_team):
        _otf2.EvtWriter_ThreadTeamEnd(self._handle, attribute_list, time, thread_team)

    def _thread_acquire_lock(self, attribute_list, time, model, lock_id, acquisition_order):
        _otf2.EvtWriter_ThreadAcquireLock(self._handle, attribute_list, time, model, lock_id, acquisition_order)

    def _thread_release_lock(self, attribute_list, time, model, lock_id, acquisition_order):
        _otf2.EvtWriter_ThreadReleaseLock(self._handle, attribute_list, time, model, lock_id, acquisition_order)

    def _thread_task_create(self, attribute_list, time, thread_team, creating_thread, generation_number):
        _otf2.EvtWriter_ThreadTaskCreate(self._handle, attribute_list, time, thread_team, creating_thread, generation_number)

    def _thread_task_switch(self, attribute_list, time, thread_team, creating_thread, generation_number):
        _otf2.EvtWriter_ThreadTaskSwitch(self._handle, attribute_list, time, thread_team, creating_thread, generation_number)

    def _thread_task_complete(self, attribute_list, time, thread_team, creating_thread, generation_number):
        _otf2.EvtWriter_ThreadTaskComplete(self._handle, attribute_list, time, thread_team, creating_thread, generation_number)

    def _thread_create(self, attribute_list, time, thread_contingent, sequence_count):
        _otf2.EvtWriter_ThreadCreate(self._handle, attribute_list, time, thread_contingent, sequence_count)

    def _thread_begin(self, attribute_list, time, thread_contingent, sequence_count):
        _otf2.EvtWriter_ThreadBegin(self._handle, attribute_list, time, thread_contingent, sequence_count)

    def _thread_wait(self, attribute_list, time, thread_contingent, sequence_count):
        _otf2.EvtWriter_ThreadWait(self._handle, attribute_list, time, thread_contingent, sequence_count)

    def _thread_end(self, attribute_list, time, thread_contingent, sequence_count):
        _otf2.EvtWriter_ThreadEnd(self._handle, attribute_list, time, thread_contingent, sequence_count)

    def _calling_context_enter(self, attribute_list, time, calling_context, unwind_distance):
        _otf2.EvtWriter_CallingContextEnter(self._handle, attribute_list, time, calling_context, unwind_distance)

    def _calling_context_leave(self, attribute_list, time, calling_context):
        _otf2.EvtWriter_CallingContextLeave(self._handle, attribute_list, time, calling_context)

    def _calling_context_sample(self, attribute_list, time, calling_context, unwind_distance, interrupt_generator):
        _otf2.EvtWriter_CallingContextSample(self._handle, attribute_list, time, calling_context, unwind_distance, interrupt_generator)

    def _io_create_handle(self, attribute_list, time, handle, mode, creation_flags, status_flags):
        _otf2.EvtWriter_IoCreateHandle(self._handle, attribute_list, time, handle, mode, creation_flags, status_flags)

    def _io_destroy_handle(self, attribute_list, time, handle):
        _otf2.EvtWriter_IoDestroyHandle(self._handle, attribute_list, time, handle)

    def _io_duplicate_handle(self, attribute_list, time, old_handle, new_handle, status_flags):
        _otf2.EvtWriter_IoDuplicateHandle(self._handle, attribute_list, time, old_handle, new_handle, status_flags)

    def _io_seek(self, attribute_list, time, handle, offset_request, whence, offset_result):
        _otf2.EvtWriter_IoSeek(self._handle, attribute_list, time, handle, offset_request, whence, offset_result)

    def _io_change_status_flags(self, attribute_list, time, handle, status_flags):
        _otf2.EvtWriter_IoChangeStatusFlags(self._handle, attribute_list, time, handle, status_flags)

    def _io_delete_file(self, attribute_list, time, io_paradigm, file):
        _otf2.EvtWriter_IoDeleteFile(self._handle, attribute_list, time, io_paradigm, file)

    def _io_operation_begin(self, attribute_list, time, handle, mode, operation_flags, bytes_request, matching_id):
        _otf2.EvtWriter_IoOperationBegin(self._handle, attribute_list, time, handle, mode, operation_flags, bytes_request, matching_id)

    def _io_operation_test(self, attribute_list, time, handle, matching_id):
        _otf2.EvtWriter_IoOperationTest(self._handle, attribute_list, time, handle, matching_id)

    def _io_operation_issued(self, attribute_list, time, handle, matching_id):
        _otf2.EvtWriter_IoOperationIssued(self._handle, attribute_list, time, handle, matching_id)

    def _io_operation_complete(self, attribute_list, time, handle, bytes_result, matching_id):
        _otf2.EvtWriter_IoOperationComplete(self._handle, attribute_list, time, handle, bytes_result, matching_id)

    def _io_operation_cancelled(self, attribute_list, time, handle, matching_id):
        _otf2.EvtWriter_IoOperationCancelled(self._handle, attribute_list, time, handle, matching_id)

    def _io_acquire_lock(self, attribute_list, time, handle, lock_type):
        _otf2.EvtWriter_IoAcquireLock(self._handle, attribute_list, time, handle, lock_type)

    def _io_release_lock(self, attribute_list, time, handle, lock_type):
        _otf2.EvtWriter_IoReleaseLock(self._handle, attribute_list, time, handle, lock_type)

    def _io_try_lock(self, attribute_list, time, handle, lock_type):
        _otf2.EvtWriter_IoTryLock(self._handle, attribute_list, time, handle, lock_type)

    def _program_begin(self, attribute_list, time, program_name, program_arguments):
        _otf2.EvtWriter_ProgramBegin(self._handle, attribute_list, time, program_name, program_arguments)

    def _program_end(self, attribute_list, time, exit_status):
        _otf2.EvtWriter_ProgramEnd(self._handle, attribute_list, time, exit_status)

    def _non_blocking_collective_request(self, attribute_list, time, request_id):
        _otf2.EvtWriter_NonBlockingCollectiveRequest(self._handle, attribute_list, time, request_id)

    def _non_blocking_collective_complete(self, attribute_list, time, collective_op, communicator, root, size_sent, size_received, request_id):
        _otf2.EvtWriter_NonBlockingCollectiveComplete(self._handle, attribute_list, time, collective_op, communicator, root, size_sent, size_received, request_id)

    def _comm_create(self, attribute_list, time, communicator):
        _otf2.EvtWriter_CommCreate(self._handle, attribute_list, time, communicator)

    def _comm_destroy(self, attribute_list, time, communicator):
        _otf2.EvtWriter_CommDestroy(self._handle, attribute_list, time, communicator)
