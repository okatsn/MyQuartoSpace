FROM okatsn/my-julia-space

USER $NB_USER
WORKDIR $WORKSPACE_DIR

COPY .devcontainer/startup_ijulia.jl /home/$NB_USER/.julia/config/startup_ijulia.jl

# ENTRYPOINT ["julia", "--project=@.", "-e", "'using Pkg; Pkg.build(\"IJulia\")'"]
# ENTRYPOINT ["julia", "--project=@.", "-e", "'using Pkg; println(pwd()); show(Pkg.status())'"]
