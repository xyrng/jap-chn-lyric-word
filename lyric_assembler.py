import sys;
import argparse;

JAP_LYRIC_FILE_PATH = None;
CHN_LYRIC_FILE_PATH = None;
MIX_LYRIC_FILE_PATH = None;
OUTPUT_FILENAME = None;




def get_input_argv():
    parser = argparse.ArgumentParser(description="Parse input file path.");
    parser.add_argument('-c', '--chinese', type=str, help='file path of Chinese lyric.');
    parser.add_argument('-j', '--japanese', type=str, help='file path of Japanese lyric.');
    parser.add_argument('-x', '--mix', type=str, help='file path of mix lyric.');
    parser.add_argument('-o', '--output', type=str, help='Output file name.');
    args = parser.parse_args();

    if args.mix and (args.chinese or args.japanese):
        parser.error("Option -x cannot be used with -c or -j.");
    elif not args.mix and not (args.chinese and args.japanese):
        parser.error("Either both -c and -j must be specified together or just -x.");

    if not args.output:
        parser.error("Output file name -o or --output must be specified.");

    if args.mix:
        MIX_LYRIC_FILE_PATH = args.mix;
    elif args.chinese:
        CHN_LYRIC_FILE_PATH = args.chinese;
        JAP_LYRIC_FILE_PATH = args.japanese;

    OUTPUT_FILENAME = args.output;

    print("output: " + OUTPUT_FILENAME)

if __name__=="__main__": 
    get_input_argv();

    