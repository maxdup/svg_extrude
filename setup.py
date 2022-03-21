from distutils.core import setup
setup(
    name='svg_extrude',
    packages=['svg_extrude', 'svg_extrude.model', 'svg_extrude.scad', 'svg_extrude.util', 'svg_extrude.css'],
    version='0.1.0',
    license='gpl-3.0',
    description='A Python SVG parser and drawing module',
    author='deffi',
    author_email='',
    url='https://github.com/deffi/svg_extrude',
    download_url='',
    keywords=['svg', 'extrude', 'stl', '3mf', 'amf', 'stl', 'scad', 'openscad'],
    install_requires=['rapidtables', 'tinycss2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Graphics :: 3D Modeling',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
