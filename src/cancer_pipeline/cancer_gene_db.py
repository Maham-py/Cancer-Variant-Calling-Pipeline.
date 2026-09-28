
#This file stores information about cancer genes
cancer_genes = {
    "TP53" : "Stops damaged cells from growing. Found in over half of cancers.",
    "BRCA1": "Helps repair damaged DNA. Mutations that raise breast and ovarian cancer risk.",
    "KRAS" : "Acts like an on-switch for cell-growth.Mutations can jam it on." }
def explain_gene(gene_name):
    if gene_name in cancer_genes:
        return cancer_genes[gene_name]
    else:
        return "Not in our cancer gene list."
print(explain_gene("TP53"))
print(explain_gene("ABC123"))
