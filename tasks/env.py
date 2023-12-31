from invoke import task

# https://github.com/pyinvoke/invoke/issues/682
@task
def julia_daemon(ctx):
    """Run julia server, that is responsible for running all julia scripts."""
    ctx.run(
        "julia --project=@. -t auto --startup-file=no -e "
        + "'using Revise; using DaemonMode; serve(async=true)'",
        disown=True
    ) # QUESTION: do Revise and DaemonMode have any cost?
    # also see
    # [Julia Development Workflow with Revise.jl](https://kdr2.com/promotion/1901-julia-dev-with-revise-jl.html)
    # [Using Revise by default](https://timholy.github.io/Revise.jl/stable/config/#Using-Revise-by-default-1)

# @task
# def setup_pre_commit_hook(ctx):
#     """Setup Git hooks with pre-commit."""
#     ctx.run("git init")
#     ctx.run("pre-commit install -t pre-commit")
#     ctx.run("pre-commit install -t pre-push")
#     ctx.run("pre-commit install -t commit-msg")
#     ctx.run("pre-commit install -t post-checkout")

# @task
# def uninstall_pre_commit_hook(ctx):
#     """Uninstall Git hooks with pre-commit."""
#     ctx.run("pre-commit uninstall -t pre-commit")
#     ctx.run("pre-commit uninstall -t pre-push")
#     ctx.run("pre-commit uninstall -t commit-msg")
#     ctx.run("pre-commit uninstall -t post-checkout")

# @task
# def julia_instantiate(ctx):
#     """Download all dependencies of the current julia project and precompile all dependencies."""
#     ctx.run("julia --project=@. -e 'using Pkg; Pkg.instantiate(); Pkg.precompile()'", pty=True)

# @task(optional=["no-pre-commit"])
# def init_dev(ctx, no_pre_commit=True):
#     """Install development dependencies, setup pre-commit hooks."""
#     julia_instantiate(ctx)
#     if no_pre_commit:
#         uninstall_pre_commit_hook(ctx)
#     else:
#         setup_pre_commit_hook(ctx)
#     ## Sync DVC
#     # ctx.run("dvc pull")
#     # ctx.run("dvc push")
