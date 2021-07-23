# Master's Thesis Outline

Peter Sharpe

-----

Title: **A Differentiable Framework for Aircraft Design Optimization**

* Front matter
	* TOC
	* Acknowledgements
* Introduction
	* One-paragraph summary of contributions
	* Motivations for Aircraft Design Optimization
		* Challenges
			* Coupled problems
				* Closure problem
			* High-dimensional problems
				* Gradient-based optimization bottlenecks
			* Dynamic systems
				* Time-dependent
	* Definitions
	* Existing approaches (and limitations) (Lit. review)
		* SUAVE
		* OpenMDAO
		* GPKit
* AeroSandbox: A Differentiable Framework
	* Summary of Features, optimization paradigm
	* Implementation details, availability, documentation, testing
	* Core stacks:
		* Opti stack
			* Automatic differentiation
				* Existing approaches (JAX, Torch)
			* SAND
				* ODEs / systems of equations
		* NumPy stack
		* Geometry stack
	* Limitations
		* Glass-box models
		* Differentiability and Continuity
* AeroSandbox: Tools and Models
	* 3D Aerodynamics
	* 2D Aerodynamics
	* Propulsion
	* Power Systems
	* Atmosphere and Winds
	* Structures and weights
	* Surrogate Modeling Tools
		* FittedModel
		* InterpolatedModel
* AeroSandbox: Validation and benchmarks
	* 
* Application: Firefly
	* Requirements and Configuration
	* Design code
	* Range Optimization Study
	* Understanding the Design Space
	* Multi-objective optimization and pareto efficiency
* Application: Dawn
	* Requirements and Configuration
	* Dawn Design Tool
		* XDSM
	* Mass budgets
	* Carpet plots and Envelope exploration
	* Cruise dynamics
	* Ascent dynamics
	* Design sensitivities
* Conclusions
	* Summary of Contributions
	* Limitations and Future work
		* Investigations of sparsity usage efficiency
		* Differentiation frameworks
			* Julia-based frameworks
		* Modeling methods
			* Finite-difference implementation
* Appendix
	* Optimization Caveats

Other thoughts

* Ability to list assumptions