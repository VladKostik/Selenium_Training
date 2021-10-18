def test_cookies(cookie):
    cookie._add_one('test cookie', 'test cookie value')
    print("\nCOOKIES:", cookie._get_one('test cookie'))
    print("\nCOOKIES:", cookie._get_all())

def test_local_storage(local_storage):
    local_storage._add_one('name', 'dataaaaa')
    print("\nLOCAL STORAGE: ", local_storage._get_one_by_name('name'))
    print("\nLOCAL STORAGE: ", local_storage._get_all())
