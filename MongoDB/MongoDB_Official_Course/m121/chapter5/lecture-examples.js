db.employees.aggregate([
	{
		$redact: {
			$cond: [{ $in: ["Management", "$acl"] }, "$$DESCEND", "$$PRUNE"],
		},
	},
]);
