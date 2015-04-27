'''
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
'''
from webassets.filter import ExternalTool, register_filter


def register():
    register_filter(NgAnnotateFilter)


class NgAnnotateFilter(ExternalTool):
    name = 'ng-annotate'
    options = {
        'binary': 'NG_ANNOTATE_BIN',
        'extra_args': 'NG_ANNOTATE_EXTRA_ARGS',
    }

    def output(self, infile, outfile, **kwargs):
        args = [self.binary or 'ng-annotate', '-a', '-']
        if self.extra_args:
            args.extend(self.extra_args)
        self.subprocess(args, outfile, infile)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
