'use strict';

/* https://github.com/angular/protractor/blob/master/docs/toc.md */

describe('DStore Test Application', function() {

  it('should redirect `index.html` to `index.html#!/cars', function() {
    browser.get('index.html');
    expect(browser.getLocationAbsUrl()).toBe('/cars');
  });

});
