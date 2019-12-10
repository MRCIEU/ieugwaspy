import ieugwaspy.query as query

def variants_to_rsid(variants):
    for pos, variant in enumerate(variants):
        if variant.find(":") > 0:
            variants[pos] = variants_chrpos(variant)
    variants = list(dict.fromkeys(variants))
    return(variants)



# variants_to_rsid <- function(variants)
# {
# 	index <- grep(":", variants)
# 	if(length(index) > 0)
# 	{
# 		o <- variants_chrpos(variants[index])$name
# 		variants <- c(o, variants[-index]) %>% unique
# 	}
# 	return(variants)
# }
