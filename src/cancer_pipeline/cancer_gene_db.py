# This file stores information about cancer genes (explanations and sources)
# website used for explanation and provided as source  "medlineplus genetics"
cancer_genes = {
    "TP53": {
        "explanation": "Stops damaged cells from growing. Found in over half of cancers.",
        "source": "https://medlineplus.gov/genetics/gene/tp53/",
    },
    "FLT3": {
        "explanation": "Signals blood cells to grow. Mutations keep it stuck 'on' in acute myeloid leukemia.",
        "source": "https://medlineplus.gov/genetics/gene/flt3/",
    },
    "NPM1": {
        "explanation": "Helps control cell growth by keeping the tumor-suppressor ARF in place. Mutated in about 64% of one AML subtype, trapping the protein outside the nucleus.",
        "source": "https://medlineplus.gov/genetics/gene/npm1/",
    },
    "KRAS": {
        "explanation": "Acts like an on-switch for cell growth. Mutations can jam it on.",
        "source": "https://medlineplus.gov/genetics/gene/kras/",
    },
    "JAK2": {
        "explanation": "Signals bone marrow to make blood cells. The V617F mutation locks it 'on', driving blood cancers like polycythemia vera and myelofibrosis.",
        "source": "https://medlineplus.gov/genetics/gene/jak2/",
    },
    "TET2": {
        "explanation": "Normally acts as a tumor suppressor in blood stem cells. Somatic mutations make it nonfunctional, linked to leukemia, myelodysplastic syndrome and other blood disorders.",
        "source": "https://medlineplus.gov/genetics/gene/tet2/",
    },
    "IDH2": {
        "explanation": "Helps cells produce energy. Somatic mutations make it produce a toxic byproduct that blocks normal blood cell maturation, found in about 20% of one AML subtype.",
        "source": "https://medlineplus.gov/genetics/gene/idh2/",
    },
    "NOTCH1": {
        "explanation": "Normally guides cell growth and self-destruction. Mutations that lock its signaling 'on' are linked to blood cancers like T-cell leukemia (T-ALL) and chronic lymphocytic leukemia (CLL).",
        "source": "https://medlineplus.gov/genetics/gene/notch1/",
    },
    "MYD88": {
        "explanation": "Normally helps immune cells respond to infection. A somatic mutation (L265P) makes it overactive, found in over 90% of Waldenstrom macroglobulinemia and linked to other B-cell lymphomas.",
        "source": "https://medlineplus.gov/genetics/gene/myd88/",
    },
}


def explain_gene(gene_name):
    if gene_name in cancer_genes:
        gene_info = cancer_genes[gene_name]
        return gene_info["explanation"] + " Source: " + gene_info["source"]
    else:
        return "Not in our cancer gene list."


print(explain_gene("MYD88"))
