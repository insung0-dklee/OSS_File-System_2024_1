def read_in_chunks(file_object, chunk_size=1024):

    Args:
        file_object (file): 읽을 파일 객체
        chunk_size (int, optional): 청크 크기. 기본값은 1024 바이트입니다.

    Yields:
        bytes: 파일 청크
    """
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


