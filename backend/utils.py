def cleanup_file(path):
    try:
        import os
        os.remove(path)
    except:
        pass
