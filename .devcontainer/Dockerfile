FROM okatsn/my-julia-space

ENTRYPOINT ["julia", "--project=@.", "-e", "using Pkg; Pkg.build(\"IJulia\")"]