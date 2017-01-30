#!/usr/bin/python

if __name__ == '__main__':
    from test_site.app import create_app
    from test_site.models import Car
    app, api = create_app( config = "test_site.configs.server" )

    with app.app_context():
        api.store.create_all()

        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2006 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2007 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2008 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2009 ).add()

    app.run( host = "0.0.0.0", port = 6000, debug = True, use_reloader = False )

    with app.app_context():
        api.store.destroy_all()
