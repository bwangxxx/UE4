# coding=gbk
import unreal

"""
Usage:

import sequencer
sequencer.NAME
sequencer.Hello()

reload(sequencer)
"""
NAME = 'wangbo'


def hello():
    """
    Only for test.
    :return:
    """

    print('========================================================================')
    print('Get LevelSequence')
    print('========================================================================')
    print('----------=WB=----------')
    sequence_path = '/Game/Seq'
    sequence_asset = unreal.LevelSequence.cast(unreal.load_asset(sequence_path))
    print('====================================')
    print '00 sequence_asset = unreal.LevelSequence.cast(unreal.load_asset("/Game/Seq")) (base=MovieSceneSequence)'
    print('====================================')
    print '\tsequence_asset  = {}'.format(sequence_asset)

    timecode_source = sequence_asset.get_timecode_source()  # Timecode
    tick_resolution = sequence_asset.get_tick_resolution()  # FPS
    display_rate = sequence_asset.get_display_rate()
    print '\ttimecode_source = {}'.format(timecode_source)
    print '\ttick_resolution = {}'.format(tick_resolution)
    print '\tdisplay_rate    = {}'.format(display_rate)
    print '\t\tdisplay_rate.numerator   = {}'.format(display_rate.numerator)
    print '\t\tdisplay_rate.denominator = {}'.format(display_rate.denominator)

    playback_start = sequence_asset.get_playback_start()
    playback_end = sequence_asset.get_playback_end()
    view_range_start = sequence_asset.get_view_range_start()
    view_range_end = sequence_asset.get_view_range_end()
    work_range_start = sequence_asset.get_work_range_start()
    work_range_end = sequence_asset.get_work_range_end()
    print '\tplayback_start   = {}'.format(playback_start)
    print '\tplayback_end     = {}'.format(playback_end)
    print '\tview_range_start = {:.0f}'.format(float(view_range_start) * float(display_rate.numerator))
    print '\tview_range_end   = {:.0f}'.format(float(view_range_end) * float(display_rate.numerator))
    print '\twork_range_start = {:.0f}'.format(float(work_range_start) * float(display_rate.numerator))
    print '\twork_range_end   = {:.0f}'.format(float(work_range_end) * float(display_rate.numerator))

    movie_scene = sequence_asset.get_movie_scene()
    marked_frames = sequence_asset.get_marked_frames()
    root_folders_in_sequence = sequence_asset.get_root_folders_in_sequence()
    spawnables = sequence_asset.get_spawnables()
    print '\tmovie_scene      = {}'.format(movie_scene)
    print '\tmarked_frames    = {}'.format(marked_frames)
    print '\troot_folders     = {}'.format(root_folders_in_sequence)
    print '\tspawnables       = {}'.format(spawnables)

    display_rate.numerator = 30
    sequence_asset.set_display_rate(display_rate)

    print('========================================================================')
    print('Get master_tracks')
    print('========================================================================')
    tracks = sequence_asset.get_master_tracks()
    print 'tracks:{}'.format(tracks)
    print 'len:{}'.format(len(tracks))
    print('====================================')
    print('01 LevelSequence.get_master_tracks()')
    print('====================================')
    for track in tracks:
        track_name = track.get_display_name()
        track_type = type(track)
        print '\ttrack_name = {0:<20} track_type = {1:}'.format(str(track_name), track_type)
        if track_type == unreal.MovieSceneCameraCutTrack:
            sections = track.get_sections()
            for section in sections:
                name = section.get_name()
                blend_type = section.get_blend_type()
                start_frame = section.get_start_frame()
                end_frame = section.get_end_frame()
                row_index = section.get_row_index
                is_active = section.is_active()
                channels = section.get_channels()
                print '\t\tsection_name  = {}'.format(name)
                print '\t\t\tblend_type  = {}'.format(blend_type)
                print '\t\t\tstart_frame = {}'.format(start_frame)
                print '\t\t\tend_frame   = {}'.format(end_frame)
                print '\t\t\trow_index   = {}'.format(row_index)
                print '\t\t\tis_active   = {}'.format(is_active)
                print '\t\t\tchannels    = {}'.format(channels)

    print('========================================================================')
    print('Get possessables')
    print('========================================================================')
    possessables = sequence_asset.get_possessables()
    print 'possessables:{}'.format(possessables)
    print 'len:{}'.format(len(possessables))
    print('====================================')
    print('02 LevelSequence.get_possessables()')
    print('====================================')
    for possessable in possessables:
        possessable_name = possessable.get_display_name()
        possessable_type = type(possessable)
        print '\tpossessable_name = {0:<20} possessable_type = {1}'.format(str(possessable_name), possessable_type)

    print('========================================================================')
    print('Get bindings')
    print('========================================================================')
    bindings = sequence_asset.get_bindings()
    print 'bindings:{}'.format(bindings)
    print 'len:{}'.format(len(bindings))
    print('====================================')
    print('03 LevelSequence.get_bindings()')
    print('====================================')
    for binding in bindings:
        parent = binding.get_parent()
        # if parent.get_name() == '':
        if parent.get_name() is not None:
            print '\tparent_name = {}'.format(parent.get_name())
            print '\tname = {}'.format(binding.get_name())

            children = binding.get_child_possessables()
            print '\t\tchildren_num = {}'.format(len(children))
            for child in children:
                print '\t\t\tchild_name = {}'.format(child.get_name())

            possessed_object_class = binding.get_possessed_object_class()
            print '\t\tpossessed_object_class = {}'.format(possessed_object_class)

            tracks = binding.get_tracks()
            print '\t\ttracks = {}'.format(tracks)
            for track in tracks:
                print '\t\t\ttrack_name = {}'.format(track.get_display_name())
                sections = track.get_sections()
                for section in sections:
                    print '\t\t\tsection_type = {}'.format(type(section))
                    is_locked = section.get_editor_property('is_locked')
                    section_range = section.get_editor_property('section_range')
                    print '\t\t\t\tsection.is_locked     = {}'.format(is_locked)
                    print '\t\t\t\tsection.section_range = {}'.format(section_range)
                    channels = section.get_channels()
                    for channel in channels:
                        print '\t\t\t\t\tchannel_name = {}'.format(channel.get_name())
                        print '\t\t\t\t\tchannel_type = {}'.format(type(channel))
                        print '\t\t\t\t\tchannel      = {}'.format(channel)
                        print '\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
                        keys = channel.get_keys()
                        for key in keys:
                            print '\t\t\t\t\t\tkey       = {}'.format(key)
                            print '\t\t\t\t\t\tkey_time  = {}'.format(key.get_time())
                            print '\t\t\t\t\t\tkey_time  = {} frame'.format(key.get_time().frame_number.value)
                            print '\t\t\t\t\t\tkey_value = {}'.format(key.get_value())
                            print '\t\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~'

    print('========================================================================')
    print('Level Sequence ??')
    print('========================================================================')
    sequence_obj = unreal.MovieSceneSequence()  # 创建？？？
    sequence_obj_name = sequence_obj.get_name()
    print 'sequence_obj = {}'.format(sequence_obj)
    print 'sequence_obj_name = {}'.format(sequence_obj_name)
    print('++++++++++++++++++++++++++++++++++++++')
