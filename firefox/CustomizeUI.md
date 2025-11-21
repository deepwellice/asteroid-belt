# Hide Firefox UI Elements

## Set Firefox to look for userChrome.css at startup

* Open `about:config`
* Enable `toolkit.legacyUserProfileCustomizations.stylesheets`

## CSS examples
```
#TabsToolbar {
  visibility: collapse;
}

#sidebar-panel-header {
  visibility: collapse !important;
}
```
