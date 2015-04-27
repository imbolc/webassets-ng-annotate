Webassets-ng-annotate
=====================
Ng-annotate filter for webassets.

Install
-------
    npm install -g ng-annotate
    pip install webassets-ng-annotate

Usage
-----
    from webassets import Bundle
    import webassets_ng_annotate

    webassets_ng_annotate.register()
    js = Bundle('vendors/angular.js', 'app.js',
                filters='ng-annotate,uglifyjs',
                output='gen/packed.js')

Parameters
----------
- `NG_ANNOTATE_BIN` - path to `ng-annotate` binary
- `NG_ANNOTATE_EXTRA_ARGS` - additional option to pass to `ng-annotate`