'''
md2html
    Convert markdown files to html

Usage:
    md2html [-i/--indir] [-r/--recurse] [-d/--outdir]
        -i/--indir: Default to cwd
        -r/--recurse: Recurse through [indir] converting *.md files
        -d/--outdir: Output dir, default to $CWD/md2html
'''
import argparse
import logging
from pathlib import Path

from markdown2 import Markdown


logging.basicConfig(level=logging.INFO)


def md2html(infile, outfile):
    markdowner = Markdown()

    with open(infile, "r") as infile:
        with open(outfile, "w") as outfile:
            outfile.write(markdowner.convert(infile.read()))


def lsdir(root, ext='', recursive=True):
    for filename in root.glob('**/*' + ext):
        logging.info(filename)
        yield filename


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--indir", help="Input directory to scan for markdown files.", type=str, default='.')
    parser.add_argument("--outdir", help="Output directory to write html files", type=str, default='md2html')
    parser.add_argument("--recurse", help="Recurse through input directory", type=bool, default=False)

    args = parser.parse_args()

    recurse = args.recurse
    indir = Path(args.indir).absolute()
    outdir = Path(args.outdir).absolute()

    logging.info('COMMANDLINE ARGS')
    logging.info('\tindir: ' + args.indir)
    logging.info('\toutdir: ' + args.outdir)
    logging.info('\trecurse: ' + str(args.recurse))

    for filename in lsdir(indir, ".md", recurse):
        logging.info(filename)
        filename = Path(filename)
        outfile = Path.joinpath(outdir, filename.parts[-2] + '-' + filename.with_suffix('.html').name)
        md2html(filename, outfile)


if __name__ == "__main__":
    main()
