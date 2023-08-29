# Build stage
FROM okatsn/my-typst-space AS build0

FROM okatsn/my-julia-space

USER $NB_USER
WORKDIR $WORKSPACE_DIR

COPY .devcontainer/startup_ijulia.jl /home/$NB_USER/.julia/config/startup_ijulia.jl

# ENTRYPOINT ["julia", "--project=@.", "-e", "'using Pkg; Pkg.build(\"IJulia\")'"]
# ENTRYPOINT ["julia", "--project=@.", "-e", "'using Pkg; println(pwd()); show(Pkg.status())'"]

# Copy the built binary from the Rust build stage to the final stage
COPY --from=build0 /bin/typst /bin
# Please refer https://github.com/okatsn/my-typst-space