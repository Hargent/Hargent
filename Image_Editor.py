# import libraries
import io


class Edit:
    '''
    rename , crop , frame , resize , filter , merge , insert_text
    '''
    def _rename_():
        '''
        Requests for a folder and renames the pictures in the folder. \n
        it requests for a folder name , creates the folder and saves the renamed images in the new folder. \n
        Also allows the user to change the extension type of the image. \n
        Created by HARGENT.
        '''
        from PIL import Image
        import os
        import time

        t1 = time.time()

        trial = 0
        while True:
            try:
                mother_path = str('C:\\Users\\SILVER\\Pictures')
                edited = str(
                    input('Enter the name of folder to store edited pictures : ')
                )
                edited_path = '\\'.join([mother_path, edited])

                os.makedirs(edited_path)
                print(edited_path)
                break

            except FileExistsError:
                print('.......')
                print(edited_path)
                break
            except OSError as err:
                print(
                    f'OSError : {err}\n Please enter a valid folder path.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
                    continue

            except ValueError as val:
                print(
                    f'ValueError : {val} \n Please enter a valid folder path.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
                    continue

        while trial >= 0:
            try:

                # file_path = str(
                #     input('Enter the folder path of pictures to be edited : ')
                # )
                while True:
                    Intro = "Please move the folder you want to edit to the pictures folder"
                    print(Intro.upper())
                    time.sleep(3)
                    _ask0 = str(input('has the folder been moved ? '))
                    if _ask0 == 'yes':

                        name = str(input('Enter the folder name : '))
                        file_path = '\\'.join([mother_path, name])
                        break
                    elif _ask0 == 'no':
                        continue

                files = os.listdir(file_path)
                count = 0
                _photos_ = []
                for file in files:
                    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.jfif'):

                        _photos_.append(file)

                    else:
                        print('Please enter a folder path that contains pictures')
                        break

                contain = len(_photos_)
                print(f'There are {contain} pictures in the choosen folder.')
                no_edited = 0
                for picture in _photos_:
                    count += 1
                    print(f'{count} . {picture}')

                    original_name = os.path.splitext(picture)[0]
                    original_name_path = os.path.relpath(picture)
                    the_path = '\\'.join([file_path, original_name_path])
                    image_ = Image.open(the_path)
                    print(f'The name of the picture is {original_name}')
                    print(the_path)
                    while no_edited > 2:
                        ask = input('Do you want to keep editing ? : ')
                        if ask == 'no' or ask == 'nah':
                            t2 = time.time()
                            t3 = time.ctime()

                            print(
                                f'You have spent {t2-t1} seconds editing...'
                            )
                            print(
                                f'The time is {t3} , go and rest Boss'
                            )
                            _ask = int(input(
                                f'Do you want to exit code or sleep ? \n To sleep , enter 1 \n To exit code, enter 0 \n sleep or exit ? : '))
                            if _ask == 1:
                                t4 = int(
                                    input('Enter the rest time in seconds : '))
                                time.sleep(t4)
                            elif _ask == 0:
                                os._exit(0)
                        elif ask == 'yes':
                            break

                    ask_1 = input(
                        'Do you want to see the picture of the image ? : ')
                    if ask_1 == 'yes' or ask_1 == 'yea' or ask_1 == 'yeah' or ask_1 == 'sure' or ask_1 == 'aye':
                        image_.show()
                    ask_2 = str(
                        input('Do you want to rename this picture ? : '))

                    if ask_2 == 'yes' or ask_2 == 'yea' or ask_2 == 'yeah' or ask_2 == 'sure' or ask_2 == 'aye':
                        while True:
                            try:
                                new_name = input('Enter the new name : ')
                                file_extension = input(
                                    'Enter the file extension : '
                                )
                                extension = file_extension.lower()
                                image_.save(
                                    f'{new_name}.{extension}'
                                )
                                image_path = str(os.path.relpath(
                                    f'{new_name}.{extension}'))
                                print(image_path)
                                new_path = '\\'.join(
                                    [edited_path, f'{new_name}.{extension}'])
                                os.renames(image_path, new_path)

                                no_edited += 1
                                c_2 = f'You have edited {no_edited} pictures'
                                break

                            except ValueError as val:
                                print(
                                    f'ValueError : {val} \n Enter a valid extension.')
                                trial = trial + 1
                                if trial % 5 == 0:
                                    time.sleep(5)

                            except OSError as osr:
                                print(
                                    f'OSError : {osr} \n Please enter a valid folder path.')
                                trial = trial + 1
                                if trial % 5 == 0:
                                    time.sleep(5)
                t5 = time.time()
                c_1 = 'Done Boss!!'
                c_3 = f'It took {t5-t1} seconds to complete the editing...'
                print(
                    f'{c_1}\n{c_2}\n{c_3}\n Check \'pictures\'for the folder containing the saved edited pictures')
                break

            except FileNotFoundError as fil:
                print(
                    f'FileNotFoundError : {fil} Please enter the name of the folder you moved.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)

            except NameError as name:
                print(
                    f'NameError : {name} Please enter the name of the folder you moved .')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
            except ValueError as val:
                print(
                    f'ValueError : {val} \n Please enter the name of the folder you moved.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
            except FileExistsError as fee:
                print(
                    f'FileExistsError : {fee} \n Please enter the name of the folder you moved.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)

    # #  crop
    # whatever u cut must be removed from the main size too
    # allow for satisfactory check

    def _crop():
        '''
        uses a square to reduce the font of an image in a folder.
        '''

        from PIL import Image
        import os
        import time

        t1 = time.time()

        trial = 0
        while True:
            try:
                mother_path = str('C:\\Users\\SILVER\\Pictures')
                edited = str(
                    input('Enter the name of folder to store edited pictures : '))
                edited_path = '\\'.join([mother_path, edited])
                os.makedirs(edited_path)
                print(edited_path)
                break
            except FileExistsError:
                print('.......')
                print(edited_path)
                break
            except ValueError as val:
                print(
                    f'ValueError : {val} \n Please enter a valid folder path.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
                    continue
            except OSError as err:
                print(f' {err} \n Enter a valid folder name')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
                continue
        while trial >= 0:
            try:

                # file_path = str(
                #     input('Enter the folder path of pictures to be edited : ')
                # )

                while True:
                    Intro = "Please move the folder you want to edit to the pictures folder"
                    print(Intro.upper())
                    time.sleep(3)
                    _ask0 = str(input('has the folder been moved ? '))
                    if _ask0 == 'yes':

                        name = str(input('Enter the folder name : '))
                        file_path = '\\'.join([mother_path, name])
                        break
                    elif _ask0 == 'no':
                        continue

                files = os.listdir(file_path)
                count = 0
                _photos_ = []
                for file in files:
                    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.jfif'):

                        _photos_.append(file)

                    else:
                        print('Please enter a folder path that contains pictures')
                        break

                contain = len(_photos_)
                print(f'There are {contain} pictures in the choosen folder.')
                no_edited = 0
                break
            except OSError as osr:
                print(
                    f'OSError : {osr} \n Please enter a valid folder path.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
            except ValueError as val:
                print(
                    f'ValueError : {val} \n Please enter a valid folder path.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
            except FileNotFoundError as fil:
                print(
                    f'FileNotFoundError : {fil} Please enter a valid folder path.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)

            except NameError as name:
                print(f'NameError : {name} Please enter a valid folder path.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
            except FileExistsError as fee:
                print(
                    f'FileExistsError : {fee} \n Please enter the name of the folder you moved.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)

        for picture in _photos_:
            count += 1
            if contain >= 5:
                while no_edited % 5 == 0:
                    ask_1 = str(input(f'Do you want to keep editing ? : '))
                    if ask_1 == 'no':
                        t2 = time.time()
                        t3 = time.ctime()

                        print(
                            f'You have spent {t2-t1} seconds editing...'
                        )
                        print(
                            f'The time is {t3} , go and rest Boss'
                        )
                        _ask = int(input(
                            f'Do you want to exit program or sleep ? \n To sleep , enter 1 \n To exit code, enter 0 \n sleep or exit ? : '))
                        if _ask == 1:
                            t4 = int(
                                input('Enter the rest time in seconds : '))
                            time.sleep(t4)
                        elif _ask == 0:
                            os._exit(0)

                    elif ask_1 == 'yes':
                        break
            print(f'{count} . {picture}')

            picss = os.path.relpath(picture)
            pic_path = '\\'.join([file_path, picss])
            pic = Image.open(pic_path)
            size = (pic.size)

            # print(size)
            print(f' The original size of the picture is {size}')
            pic.show()

            length = size[0]
            width = size[1]
            print(
                f'The length of the picture is {length} \n The width of the picture is {width}')

            while True:

                while True:
                    while True:
                        try:
                            crop_length = int(
                                input('Enter the value for the crop length : '))
                            crop_width = int(
                                input('Enter the value for the crop width : '))
                            break
                        except ValueError as val:
                            print(f'{val} \n Enter a valid number')
                            trial = trial + 1
                            if trial % 5 == 0:
                                time.sleep(5)
                            continue

                    if crop_length > 0 and crop_width > 0:
                        try:
                            new_grid_length = length - crop_length
                            new_grid_width = width - crop_width
                            print(new_grid_length, new_grid_width)
                            cropped_pic = pic.crop(
                                (crop_length, crop_width, new_grid_length, new_grid_width))
                            break
                        except SystemError as sys:
                            print(
                                f'SystemError : {sys} \n Enter a smaller crop length and width')
                            trial = trial + 1
                            if trial % 5 == 0:
                                time.sleep(5)
                            continue
                        except ValueError as val:
                            print(
                                f'ValueError : {val} \n Please enter a valid folder path.')
                            trial = trial + 1
                            if trial % 5 == 0:
                                time.sleep(5)
                    else:
                        continue

                cropped_pic.show()
                ask = str(
                    input('Are you satisfied with the edited picture ? :'))
                if ask == 'no':
                    continue
                elif ask == 'yes':
                    no_edited = no_edited + 1
                    cropped_image_name = input(
                        'Enter the new name for the cropped image : ')
                    while True:

                        cropped_image_extension = input(
                            'Enter the file extension for the cropped image : '
                        )
                        print('Alright \n saving your cropped image .....')

                        try:
                            extension = cropped_image_extension.lower()
                            cropped_pic.save(
                                f'{cropped_image_name}.{extension}'
                            )
                            break
                        except OSError as osr:
                            print(
                                f'OSError : {osr} \n Enter a valid file extension.')
                            trial = trial + 1
                            if trial % 5 == 0:
                                time.sleep(5)
                            continue
                        except ValueError as val:
                            print(
                                f'ValueError : {val} \n Please enter a valid folder path.')
                            trial = trial + 1
                            if trial % 5 == 0:
                                time.sleep(5)

                    cropped_pic_path = str(os.path.relpath(
                        f'{cropped_image_name}.{extension}'))
                    print(cropped_pic_path)
                    new_cropped_pic_path = '\\'.join(
                        [edited_path, f'{cropped_image_name}.{extension}'])
                    os.renames(cropped_pic_path, new_cropped_pic_path)

                    print(f'Your image has been saved in {edited}')

                    break
                t = time.time()
                time_taken = t - t1
                print(
                    f'All the pictures in this folder has been successfully cropped.\n It took  {time_taken} to complete the operation.')

    def _frame():
        '''Uses an expanded square to create a frame for the pictures in the selected folder.'''
        from PIL import Image
        import os
        import time

        t1 = time.time()

        trial = 0
        while True:
            try:
                mother_path = str('C:\\Users\\SILVER\\Pictures')
                edited = str(
                    input('Enter the name of folder to store edited pictures : '))
                edited_path = '\\'.join([mother_path, edited])
                os.makedirs(edited_path)
                print(edited_path)
                break
            except FileExistsError:
                print('.......')
                print(edited_path)
                break
            except ValueError as val:
                print(
                    f'OSError : {val} \n Please enter a valid folder path.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
                continue
            except OSError as osr:
                print(f'OSError : {osr} \n Enter a valid folder name.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
                continue
        while trial >= 0:
            try:

                # file_path = str(
                #     input('Enter the folder path of pictures to be edited : ')
                # )
                while True:
                    Intro = "Please move the folder you want to edit to the pictures folder"
                    print(Intro.upper())
                    time.sleep(3)
                    _ask0 = str(input('has the folder been moved ? '))
                    if _ask0 == 'yes':

                        name = str(input('Enter the folder name : '))
                        file_path = '\\'.join([mother_path, name])
                        break
                    elif _ask0 == 'no':
                        continue

                files = os.listdir(file_path)
                count = 0
                _photos_ = []
                for file in files:
                    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.jfif'):

                        _photos_.append(file)

                    else:
                        print('Please enter a folder path that contains pictures')
                        break

                contain = len(_photos_)
                print(f'There are {contain} pictures in the choosen folder.')
                no_edited = 0
                break
            except OSError as osr:
                print(
                    f'OSError : {osr} \n Please enter a valid folder path.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
            except ValueError as val:
                print(
                    f'ValueError : {val} \n Please enter a valid folder path.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
            except FileNotFoundError as fil:
                print(
                    f'FileNotFoundError : {fil} Please enter a valid folder path.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)

            except NameError as name:
                print(f'NameError : {name} Please enter a valid folder path.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
            except FileExistsError as fee:
                print(
                    f'FileExistsError : {fee} \n Please enter the name of the folder you moved.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)

        for picture in _photos_:
            count += 1
            if contain >= 5:
                while no_edited % 5 == 0:
                    ask_1 = str(input(f'Do you want to keep editing ? : '))
                    if ask_1 == 'no':
                        t2 = time.time()
                        t3 = time.ctime()

                        print(
                            f'You have spent {t2-t1} seconds editing...'
                        )
                        print(
                            f'The time is {t3}.'
                        )
                        _ask = int(input(
                            f'Do you want to exit program or sleep ? \n To sleep , enter 1 \n To exit code, enter 0 \n sleep or exit ? : '))
                        if _ask == 1:
                            t4 = int(
                                input('Enter the rest time in seconds : '))
                            time.sleep(t4)
                        elif _ask == 0:
                            os._exit(0)

                    elif ask_1 == 'yes':
                        break
            print(f'{count} . {picture}')

            picss = os.path.relpath(picture)
            pic_path = '\\'.join([file_path, picss])
            pic = Image.open(pic_path)
            size = (pic.size)

            # print(size)
            print(f' The original size of the picture is {size}')
            pic.show()

            length = size[0]
            width = size[1]
            print(
                f'The length of the picture is {length} \n The width of the picture is {width}')

            while True:

                while True:
                    while True:
                        try:
                            frame_length = int(
                                input('Enter the value for the frame length : '))
                            frame_width = int(
                                input('Enter the value for the frame width : '))
                            break
                        except ValueError as val:
                            print(
                                f' ValueError : {val} \n Enter a valid number.')
                            trial = trial + 1
                            if trial % 5 == 0:
                                time.sleep(5)
                    if frame_length > 0 and frame_width > 0:
                        try:
                            new_grid_length = length + frame_length
                            new_grid_width = width + frame_width
                            print(new_grid_length, new_grid_width)
                            framed_pic = pic.crop(
                                ((0-frame_length), (0-frame_width), new_grid_length, new_grid_width))
                            break
                        except SystemError as sys:
                            print(
                                f'SystemError : {sys} \n Enter a smaller frame length and width')
                            trial = trial + 1
                            if trial % 5 == 0:
                                time.sleep(5)
                            continue
                        except ValueError as val:
                            print(
                                f'ValueError : {val} \n Please enter a valid folder path.')
                            trial = trial + 1
                            if trial % 5 == 0:
                                time.sleep(5)
                    else:
                        continue

                framed_pic.show()
                ask = str(
                    input('Are you satisfied with the edited picture ? :'))
                if ask == 'no':
                    continue
                elif ask == 'yes':
                    no_edited = no_edited + 1
                    framed_image_name = input(
                        'Enter the new name for the framed image : ')
                    while True:
                        framed_image_extension = input(
                            'Enter the file extension for the framed image : '
                        )
                        print('Alright \n saving your framed image .....')

                        try:
                            extension = framed_image_extension.lower()
                            framed_pic.save(
                                f'{framed_image_name}.{extension}'
                            )
                            break
                        except OSError as osr:
                            print(
                                f'OSError : {osr} \n Enter a valid file extension')
                            trial = trial + 1
                            if trial % 5 == 0:
                                time.sleep(5)
                            continue
                        except ValueError as val:
                            print(
                                f'ValueError : {val} \n Please enter a valid folder path.')
                            trial = trial + 1
                            if trial % 5 == 0:
                                time.sleep(5)
                    framed_pic_path = str(os.path.relpath(
                        f'{framed_image_name}.{extension}'))
                    print(framed_pic_path)
                    new_framed_pic_path = '\\'.join(
                        [edited_path, f'{framed_image_name}.{extension}'])
                    os.renames(framed_pic_path, new_framed_pic_path)

                    print(f'Your image has been saved in {edited}')

                    break
        t = time.time()
        time_taken = t - t1
        print(
            f'All the pictures in this folder has been successfully framed.\n It took  {time_taken} to complete the operation.')

    # # resize
    def _resize():
        '''
        re-sizes the size of each file in the folder in bytes.
        '''
        from PIL import Image
        import os
        import time

        t1 = time.time()

        trial = 0
        while True:
            try:
                mother_path = str('C:\\Users\\SILVER\\Pictures')
                edited = str(
                    input('Enter the name of folder to store edited pictures : '))
                edited_path = '\\'.join([mother_path, edited])
                os.makedirs(edited_path)
                print(edited_path)
                break
            except FileExistsError:
                print('.......')
                print(edited_path)
                break
            except ValueError as val:
                print(
                    f'OSError : {val} \n Please enter a valid folder path.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
                continue
            except OSError as osr:
                print(f'OSError : {osr} \n Enter a valid folder name.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
                continue
        while trial >= 0:
            try:

                # file_path = str(
                #     input('Enter the folder path of pictures to be edited : ')
                # )
                while True:
                    Intro = "Please move the folder you want to edit to the pictures folder"
                    print(Intro.upper())
                    time.sleep(3)
                    _ask0 = str(input('has the folder been moved ? '))
                    if _ask0 == 'yes':

                        name = str(input('Enter the folder name : '))
                        file_path = '\\'.join([mother_path, name])
                        break
                    elif _ask0 == 'no':
                        continue

                files = os.listdir(file_path)
                count = 0
                _photos_ = []
                for file in files:
                    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.jfif'):

                        _photos_.append(file)

                    else:
                        print('Please enter a folder path that contains pictures')
                        break

                contain = len(_photos_)
                print(f'There are {contain} pictures in the choosen folder.')
                no_edited = 0
                break
            except OSError as osr:
                print(
                    f'OSError : {osr} \n Please enter a valid folder path.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
            except ValueError as val:
                print(
                    f'ValueError : {val} \n Please enter a valid folder path.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
            except FileNotFoundError as fil:
                print(
                    f'FileNotFoundError : {fil} Please enter a valid folder path.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)

            except NameError as name:
                print(f'NameError : {name} Please enter a valid folder path.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
            except FileExistsError as fee:
                print(
                    f'FileExistsError : {fee} \n Please enter the name of the folder you moved.')
                trial = trial + 1
                if trial % 5 == 0:
                    time.sleep(5)
        for picture in _photos_:
            count += 1
            if contain >= 5:
                while no_edited % 5 == 0:
                    ask_1 = str(input(f'Do you want to keep editing ? : '))
                    if ask_1 == 'no':
                        t2 = time.time()
                        t3 = time.ctime()

                        print(
                            f'You have spent {t2-t1} seconds editing...'
                        )
                        print(
                            f'The time is {t3}.'
                        )
                        _ask = int(input(
                            f'Do you want to exit program or sleep ? \n To sleep , enter 1 \n To exit code, enter 0 \n sleep or exit ? : '))
                        if _ask == 1:
                            t4 = int(
                                input('Enter the rest time in seconds : '))
                            time.sleep(t4)
                        elif _ask == 0:
                            os._exit(0)

                    elif ask_1 == 'yes':
                        break
            print(f'{count} . {picture}')

            picss = os.path.relpath(picture)
            pic_path = '\\'.join([file_path, picss])
            pic = Image.open(pic_path)
            _size = os.path.getsize(pic_path)
            pic.show()
            print(_size)
            length = int(input('Enter the desired length : '))
            width = int(input("Enter the desired width : "))
            pic.thumbnail((length, width))
            pic.show()

            new_size = os.path.getsize(pic_path)
            print(f'new size is {new_size}')

            # install zipfile module


# Edit._rename_()
# Edit._crop()
# Edit._frame()
Edit._resize()

# # filter
# def _filter(*args):
#     return

#     return
# # smooth
# def _texture():
#     return
# # merge_pictures
# def _merge():
#     return
# # add writings
# def _write():
#     return
# # test
