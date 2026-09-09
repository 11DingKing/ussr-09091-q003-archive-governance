package org.example.archive;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class DomainRecordTest {
    @Test void invalidRowsRemainVisible() {
        var row = new DomainRecord("row-7", java.util.List.of("尺寸格式不一致"));
        assertFalse(row.valid());
        assertEquals("row-7", row.id());
    }
}
