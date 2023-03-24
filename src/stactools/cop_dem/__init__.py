from stactools.core import io

io.use_fsspec()


def register_plugin(registry):
    from stactools.cop_dem import commands
    registry.register_subcommand(commands.create_cop_dem_command)


__version__ = "0.2.1"
