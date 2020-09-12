from datargs.make import argsclass, arg, parse, make_parser
from tests.test_parser import ParserTest


def test_help():
    parser_help = "Program documentation"
    program = "My prog"
    parser = ParserTest(description=parser_help, prog=program)
    help_string = parser.format_help()
    assert parser_help in help_string
    assert program in help_string

    @argsclass
    class Args:
        flag: bool = arg(help="helpful message")

    args = parse(Args, [])
    assert not args.flag
    parser = make_parser(Args, parser)
    help_string = parser.format_help()
    assert "helpful message" in help_string
    assert parser_help in help_string
    assert program in help_string


def test_decorator_no_args():
    @argsclass
    class Args:
        flag: bool = arg(help="helpful message")

    assert not parse(Args, []).flag


def test_decorator_with_args():
    @argsclass(repr=True)
    class Args:
        flag: bool = arg(help="helpful message")

    assert not parse(Args, []).flag


def test_default():
    @argsclass
    class Args:
        x: int = arg(default=0)

    assert Args().x == 0


def test_alias():
    @argsclass
    class Args:
        num: int = arg(aliases=["-n"])

    args = parse(Args, ["-n", "0"])
    assert args.num == 0
